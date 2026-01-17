"""RSA Algorithm.
User should be able to enter a message that they want to Encrypt or Decrypt. 
They should have the option to use their own keys, if not the system should provide its own.
"""
from tkinter import messagebox
def greatest_common_divisor(a,b):
    return a if b==0 else greatest_common_divisor(b, a%b)

def calculate_modular_inverse(e, phi):
    """
    Calculates the modular inverse of e % phi
    d= e*d % phi=1
    
    Args:
        e (int): e is the exponent which is used in the key generation
        phi (int): Eulers totient function value
    Returns:
        d (int): The modular invese of e % phi

    I used a Extended Euclidean Algorithm to help with this implementation from online, Code was adapated:
    https://www.geeksforgeeks.org/python/python-program-for-basic-and-extended-euclidean-algorithms-2/
    """
    def extended_gcd(a, b):
        if a==0:
            return b, 0, 1
        gcd, x1, y1, =extended_gcd(b % a, a)
        x= y1- (b//a) *x1
        y=x1
        return gcd, x, y

    if greatest_common_divisor(e, phi) !=1:
        return -1 # A modular inverse doesnt exist
        
    gcd, x, y= extended_gcd(e, phi)
    return x % phi

def is_prime(given_number):
    """
    Docstring for is_prime
    
    :param given_number: Description
    """
    if given_number <=1:
        return False
    
    if given_number % 2==0 and given_number !=2:
        return False

    for i in range(3, int(given_number**.5)+1,2):
        if given_number % i==0:
            return False
    
    return True
    

def key_generation(user_p=0, user_q=0, user_e=65537):
    """
    This function generates the public and private keys for the RSA algorithm.
    As well as this, the user will be able to input their own keys if they wish to, and this function will validate them.

    The Key Generation process involes:
        1. Choosing two distinct (and usally large) prime numbers, p and q.
        2. Using p & q to computer n= p*q, where n is used in both the public and private keys.
        3. Computing Eulers totient: phi(n)= (p-1)(q-1)
        4. Choose an exponent e, such that 1< e < Eulers totient function and GCD(e, Eulers totient function)=1
        5. Calculate the decrytpion exponent d, such that d*e mod Eulers totient=1

    This Leads the the Public Key= (e,n), and the Private Key= (d,n)
    Args:
        user_p (int) | None: The user's chosen prime number (p)
        user_q (int) | None: The user's chosen prime number (q)

    Returns:
        List[bool, int, int, int, int]: A list containing if the keys are valid, the exponent e, n, exponent d, and p & q

    These sites were used to help with the explanation and implementation of this:
    https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/
    https://www.geeksforgeeks.org/dsa/eulers-totient-function/
    https://cryptographyacademy.com/rsa/
    """
    #The default values
    exponent_e= 65537 
    auto_p = 53089
    auto_q = 599426473 

    #Setting p, q and e from the users input(if selected), otherwise defaults to the set ones
    p= auto_p if user_p==0 else user_p
    q=auto_q if user_q==0 else user_q

    #Validating p and q
    if not (is_prime(p) and is_prime(q) and p!=q):
        return [False, 0,0, 0, 0]
    #Calculating n and Eulers totient, which will be used for the prime keys
    n= p * q
    euluers_totient=(p-1)*(q-1)

    
    exponent_e= user_e

    #Validating exponent_e
    if not (1 < exponent_e < euluers_totient and greatest_common_divisor(exponent_e, euluers_totient)==1):
        messagebox.showinfo("Key Generation Error", "The chosen exponent e is invalid. For e to be valid, it must be 1< e < eulers totient and GCD=1")
        return [False, 0, 0, 0, 0, 0]
    
    #Calculate d using modulve inversion
    exponent_d=calculate_modular_inverse(exponent_e, euluers_totient)

    #Final Validation to make sure d exists. If so, all values are returned to encryption/decryption
    if exponent_d== -1:
        messagebox.showinfo("Key Generation Error", "Modular Inverse doestn exist for the chosen e and Eulers totient")
        return [False, 0, 0, 0, 0, 0]
    
    
    return [True, exponent_e, n, exponent_d, p, q]

def calculate_power(integer, exponent, mod):
    """
    Calculates the power of an integer, if provided with an exponent and mod value.
    The mod value is used to make sure the integer doesnt become exponentally large, which could crash/freeze the program

    Args:
        integer (int): The base value (i.e base^exponent)
        exponent (int): The power value(i.e base^exponent)
        mod (int): Mod value which keep the integer from being too big
    Returns:
        result (int): The power value that was calculated
    """
    result=1
    integer= integer % mod
    while exponent >0:
        if exponent % 2 ==1:
            result= (result* integer) % mod
        exponent=exponent //2
        integer= (integer* integer) % mod
    
    return result

def encryption(plaintext, exponent_e, n):
    """
    Docstring for encryption
    
    :param plaintext: Description
    :param exponent_e: Description
    :param n: Description
    """
    cipher_text=[]
    for char in plaintext:
        message=ord(char)
        encrypted_char=calculate_power(message, exponent_e, n)
        cipher_text.append(encrypted_char)


    return cipher_text

def decryption(cipher_text,d, n):
    """
    Docstring for decryption
    
    :param cipher_text: Description
    :param d: Description
    :param n: Description
    """
    plaintext=[]
    for char in cipher_text:
        plaintext_char = calculate_power(char, d, n)
        plaintext.append(chr(plaintext_char))

    return "".join(plaintext)

