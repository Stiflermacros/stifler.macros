"""
Simple test file for stifler.macros repository
"""


def test_basic():
    """Basic test to verify testing infrastructure works"""
    assert True, "Basic test should always pass"


def test_addition():
    """Test basic addition"""
    result = 1 + 1
    assert result == 2, "1 + 1 should equal 2"


def test_string_concatenation():
    """Test string concatenation"""
    result = "hello" + " " + "world"
    assert result == "hello world", "String concatenation should work"


if __name__ == "__main__":
    # Run tests when executed directly
    print("Running tests...")
    
    try:
        test_basic()
        print("✓ test_basic passed")
    except AssertionError as e:
        print(f"✗ test_basic failed: {e}")
    
    try:
        test_addition()
        print("✓ test_addition passed")
    except AssertionError as e:
        print(f"✗ test_addition failed: {e}")
    
    try:
        test_string_concatenation()
        print("✓ test_string_concatenation passed")
    except AssertionError as e:
        print(f"✗ test_string_concatenation failed: {e}")
    
    print("\nAll tests completed!")
