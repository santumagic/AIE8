from fastmcp import Client

async def main():
    # Connect via stdio to the local server
    async with Client("server.py") as client:
        # List all available tools
        tools = await client.list_tools()
        print("=" * 60)
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool}")
        print("=" * 60)
        
        # Test 1: Basic Password (default settings)
        print("\n🔐 Test 1: Basic Password (16 chars, all types)")
        result = await client.call_tool("generate_password", {})
        print(f"Result: {result}")
        
        # Test 2: Custom Length (20 characters)
        print("\n🔐 Test 2: Custom Length (20 characters)")
        result = await client.call_tool("generate_password", {"length": 20})
        print(f"Result: {result}")
        
        # Test 3: No Special Characters
        print("\n🔐 Test 3: No Special Characters")
        result = await client.call_tool("generate_password", {
            "length": 16,
            "include_special": False
        })
        print(f"Result: {result}")
        
        # Test 4: Only Letters (12 chars)
        print("\n🔐 Test 4: Only Letters (12 characters)")
        result = await client.call_tool("generate_password", {
            "length": 12,
            "include_uppercase": True,
            "include_lowercase": True,
            "include_digits": False,
            "include_special": False
        })
        print(f"Result: {result}")
        
        # Test 5: Only Digits (8 chars - like a PIN)
        print("\n🔐 Test 5: Only Digits (8 chars - like a PIN)")
        result = await client.call_tool("generate_password", {
            "length": 8,
            "include_uppercase": False,
            "include_lowercase": False,
            "include_digits": True,
            "include_special": False
        })
        print(f"Result: {result}")
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

