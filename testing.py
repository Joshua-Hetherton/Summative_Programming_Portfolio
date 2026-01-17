import time

import rsa_encryption
import nth_fib
import sorting
import brute_force_merge
import random_deck
import factorial_calc
import search
import palindrome

import behavioural
import structural
import creational

def test_brute_force_merge():
    try:
        print("Commencing Merge Sort Tests...")
        assert brute_force_merge.merge_sort([5,2,1,4,2,3,6,100,-5]) == [-5,1,2,2,3,4,5,6,100]
    except AssertionError:
        print("Merge Sort Test Failed!")


def test_factorial_calc():
    try:
        print("Commencing Factorial Tests...")
        assert factorial_calc.calculate_factorial(0)==1
        assert factorial_calc.calculate_factorial(1)==1
        assert factorial_calc.calculate_factorial(2)==2
        assert factorial_calc.calculate_factorial(3)==6
        assert factorial_calc.calculate_factorial(4)==24
        assert factorial_calc.calculate_factorial(5)==120
        assert factorial_calc.calculate_factorial(6)==720

    except AssertionError:
        print("Factorial Test Failed!")
    

def test_nth_fib():
    try:
        print("Commencing Fibonacci Tests...")
        assert nth_fib.fibonacci(0)==0
        assert nth_fib.fibonacci(1)==1
        assert nth_fib.fibonacci(5)==5
        assert nth_fib.fibonacci(11)==89
        assert nth_fib.fibonacci(20)==6765
    except AssertionError:
        print("Fibonacci Test Failed!")

def test_palindrome_substrings_count():
    try:
        print("Commencing Palindrome Substring Tests...")
        assert palindrome.palindrome_substrings_count("a")==1
        assert palindrome.palindrome_substrings_count("aa")==3
        assert palindrome.palindrome_substrings_count("ab")==2
        assert palindrome.palindrome_substrings_count("abba")==6
        assert palindrome.palindrome_substrings_count("abcdef")==6
        assert palindrome.palindrome_substrings_count("aaaa")==10
    except AssertionError:
        print("Palindrome Substring Counter Test Failed!")

def test_random_deck():
    try:
        print("Commencing Random Deck Tests...")
        deck= random_deck.create_deck()
        shuffled_deck= random_deck.Fisher_yates_shuffle(deck.copy())
        assert len(deck) ==52
        assert deck != shuffled_deck
        assert len(shuffled_deck) ==52
    except AssertionError:
        print("Random Deck Test Failed")

def test_rsa_encryption():
    try:
        print("Commencing RSA Encryption Tests...")
        #Key Generation Test with no User input:
        valid, e, n, d, p, q= rsa_encryption.key_generation(0, 0)
        assert valid==True
        assert rsa_encryption.is_prime(p)==True
        assert rsa_encryption.is_prime(q)==True
        
        #Encryption and Decryption Tests:
        message="Hello World!"
        cipher_text=rsa_encryption.encryption(message, e, n)
        decrypted_message=rsa_encryption.decryption(cipher_text, d, n)
        assert message==decrypted_message

        #Key Generation Test WITH user input:
        valid, e, n, d, p, q= rsa_encryption.key_generation(7727, 7741)
        assert valid==True
        assert rsa_encryption.is_prime(p)==True
        assert rsa_encryption.is_prime(q)==True
        message="Hello World"
        cipher_text=rsa_encryption.encryption(message, e, n)
        decrypted_message=rsa_encryption.decryption(cipher_text, d, n)
        assert message==decrypted_message

    except AssertionError:
        print("RSA Encryption Test Failed!")


def test_search():
    try:
        print("Commencing Search Tests...")
        #Normal Array
        assert search.calculate_statistics([1,2,2,3,4,5,5,6,7,8])==[1,8,2,4.5,2,6]
        #Array with the same Numbers
        assert search.calculate_statistics([1,1,1,1,1,1])==[1,1,1,1.0,1,1]
        #Odd Length Array
        assert search.calculate_statistics([1,2,2,3,4,5,5,6,7])==[1,7,2,4,2.0,5.5]
    except AssertionError:
        print("Search Test Failed")

def test_sorting():
    try:
        print("Commencing Sorting Tests...")
        assert sorting.bubble_sort([1,5,2,3,-1,0], Ascending=True)==[-1,0,1,2,3,5]
        assert sorting.bubble_sort([1,5,2,3,-1,0], Ascending=False)==[5,3,2,1,0,-1]
    except AssertionError:
        print("Sorting Test Failed")

def test_behavioral():
    try:
        spacecraft=behavioural.Spacecraft()
        assert spacecraft.state.name()=="Prelaunch"
        spacecraft.transition_to_next_state()
        assert spacecraft.state.name()=="Launch"
        spacecraft.transition_to_next_state()
        assert spacecraft.state.name()=="Orbit"
        spacecraft.transition_to_next_state()
        assert spacecraft.state.name()=="Re-Entry"
    except AssertionError:
        print("Behavioral Design Pattern Test Failed")

def test_structural():
    try:
        original_measurement=structural.OriginalMeasurement(10, "feet")
        adapted_value=structural.MeasurementAdapter.convert_to_meters(original_measurement)
        assert adapted_value == 3.048
    except AssertionError:
        print("Structural Design Pattern Test Failed")

def test_creational():
    try:
        prototype_manager=creational.PrototypeManager()
        engine_types=prototype_manager.get_engine_types()
        assert "Liquid Fuel Rocket Engine" in engine_types
        assert "Solid Fuel Rocket Engine" in engine_types
        custom_engine=prototype_manager.create_custom_engine("Sea Level LF Engine", "Liquid Fuel Rocket Engine", ["Turbo Pump", "Extra Long Nozzle"])
        assert custom_engine.name=="Sea Level LF Engine"
        assert custom_engine.fuel_type=="LF-1"
        assert "Turbo Pump" in custom_engine.features
        assert "Extra Long Nozzle" in custom_engine.features
        
    except AssertionError:
        print("Creational Design Pattern Test Failed")
def call_all_tests():
    test_brute_force_merge()
    test_factorial_calc()
    test_nth_fib()
    test_palindrome_substrings_count()
    test_random_deck()
    test_rsa_encryption()
    test_search()
    test_sorting()
    test_behavioral()
    test_structural()
    test_creational()

if __name__ == "__main__":
    call_all_tests()
    pass


