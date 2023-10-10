/*package whatever //do not write package name here */

/*
* Java program for RSA asymmetric cryptographic algorithm.
* For demonstration, values are
* relatively small compared to practical application
*/
public class RSA {
public static int gcd(int a, int b)
{
	/*
		* This function returns the gcd or greatest common
		* divisor
		*/
	int temp;
	while (true) {
		temp = a % b;
		if (temp == 0)
			return b;
		a = b;
		b = temp;
	}
}
public static void main(String[] args)
{
	int p = 3;
	int q = 7;

	// Stores the first part of public key:
	int n = p * q;

	// Finding the other part of public key.
	// double e stands for encrypt
	int e = 2;
	int phi = (p - 1) * (q - 1);
	while (e < phi) {
		/*
				* e must be co-prime to phi and
				* smaller than phi.
				*/
		if (gcd(e, phi) == 1)
			break;
		else
			e++;
	}
	int k = 2; // A constant value
	int d = (1 + (k * phi)) / e;

	// Message to be encrypted
	int msg = 12;

	System.out.println("Message data = " + msg);

	// Encryption c = (msg ^ e) % n
	int c = (int)Math.pow(msg, e);
	c = c % n;
	System.out.println("Encrypted data = " + c);

	// Decryption m = (c ^ d) % n
	int m =(int)Math.pow(c, d);
	m = m % n;
	System.out.println("Original Message Sent = " + m);
}
}

// This code is contributed by Pranay Arora.
