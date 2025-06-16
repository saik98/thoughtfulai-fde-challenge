def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length

    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def run_tests():
    test_cases = [
        ((100, 100, 100, 10), "SPECIAL"),      
        ((200, 50, 50, 10), "SPECIAL"),         
        ((50, 50, 50, 25), "SPECIAL"),          
        ((200, 200, 200, 30), "REJECTED"),      
        ((149, 149, 149, 19.9), "SPECIAL"),    
        ((150, 50, 50, 10), "SPECIAL"),         
        ((100, 100, 100, 20), "REJECTED"),       
        ((150, 150, 150, 20), "REJECTED"), 
    ]

    for idx, ((w, h, l, m), expected) in enumerate(test_cases, start=1):
        result = sort(w, h, l, m)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx}: PASSED – sort({w}, {h}, {l}, {m}) → {result}")


if __name__ == "__main__":
    run_tests()