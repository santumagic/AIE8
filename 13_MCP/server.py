from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import os
from dice_roller import DiceRoller

load_dotenv()

mcp = FastMCP("mcp-server")
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for information about the given query"""
    search_results = client.get_search_context(query=query)
    return search_results

@mcp.tool()
def roll_dice(notation: str, num_rolls: int = 1) -> str:
    """Roll the dice with the given notation"""
    roller = DiceRoller(notation, num_rolls)
    return str(roller)

"""
Password Generator Tool - Creates secure random passwords with customizable criteria
"""
@mcp.tool()
def generate_password(
    length: int = 16,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_digits: bool = True,
    include_special: bool = True
) -> str:
    """
    Generate a secure random password with customizable criteria.
    
    Args:
        length: Length of the password (default: 16)
        include_uppercase: Include uppercase letters A-Z (default: True)
        include_lowercase: Include lowercase letters a-z (default: True)
        include_digits: Include digits 0-9 (default: True)
        include_special: Include special characters !@#$%^&*() (default: True)
    
    Returns:
        A randomly generated secure password as a string
    """
    import random
    import string
    
    # Build character pool based on user preferences
    character_pool = ""
    
    # Add uppercase letters if requested
    if include_uppercase:
        character_pool += string.ascii_uppercase  # A-Z
    
    # Add lowercase letters if requested
    if include_lowercase:
        character_pool += string.ascii_lowercase  # a-z
    
    # Add digits if requested
    if include_digits:
        character_pool += string.digits  # 0-9
    
    # Add special characters if requested
    if include_special:
        character_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Check if at least one character type is selected
    if not character_pool:
        return "Error: Must select at least one character type!"
    
    # Ensure length is valid
    if length < 4:
        return "Error: Password length must be at least 4 characters!"
    
    # Generate random password by selecting random characters from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    # Return the generated password
    return f"Generated Password: {password}\nLength: {len(password)} characters"

"""
Currency Converter Tool - Convert amounts between different currencies
Uses ExchangeRate-API (exchangerate-api.com) - Free tier available, no signup required for basic usage
"""
@mcp.tool()
def convert_currency(
    amount: float = 100.0,
    from_currency: str = "USD",
    to_currency: str = "EUR"
) -> str:
    """
    Convert an amount from one currency to another using real-time exchange rates.
    
    Args:
        amount: The amount to convert (default: 100.0)
        from_currency: Source currency code (e.g., USD, EUR, GBP) - default: USD
        to_currency: Target currency code (e.g., EUR, JPY, INR) - default: EUR
    
    Returns:
        Conversion result with exchange rate information
    """
    import requests
    
    # Validate amount
    if amount <= 0:
        return "Error: Amount must be greater than 0!"
    
    # Convert currency codes to uppercase
    from_curr = from_currency.upper()
    to_curr = to_currency.upper()
    
    try:
        # ExchangeRate-API free tier endpoint (no API key required for basic usage)
        # Using the open/free endpoint
        url = f"https://open.er-api.com/v6/latest/{from_curr}"
        
        # Send GET request
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code != 200:
            return f"Error: API request failed with status code {response.status_code}"
        
        # Parse JSON response
        data = response.json()
        
        # Check if API call was successful
        if data.get("result") != "success":
            return f"Error: {data.get('error-type', 'Unknown error occurred')}"
        
        # Get exchange rates
        rates = data.get("rates", {})
        
        # Check if target currency exists
        if to_curr not in rates:
            available = ", ".join(list(rates.keys())[:10]) + "..."
            return f"Error: Currency '{to_curr}' not found. Available currencies: {available}"
        
        # Calculate converted amount
        exchange_rate = rates[to_curr]
        converted_amount = amount * exchange_rate
        
        # Format the response beautifully
        result = f"💱 Currency Conversion\n"
        result += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        result += f"Amount: {amount:,.2f} {from_curr}\n"
        result += f"Converted: {converted_amount:,.2f} {to_curr}\n"
        result += f"Exchange Rate: 1 {from_curr} = {exchange_rate:.6f} {to_curr}\n"
        
        # Add last update time if available
        if "time_last_update_utc" in data:
            result += f"Last Updated: {data['time_last_update_utc']}\n"
        
        return result
        
    except requests.exceptions.RequestException as e:
        return f"Error: Network request failed - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")