package tcp;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {
	public static void main(String[]args) throws UnknownHostException, IOException {
		Socket s=new Socket("localhost",3000);
		DataOutputStream dout=new DataOutputStream(s.getOutputStream());
		DataInputStream din=new DataInputStream(s.getInputStream());
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		Scanner sc=new Scanner(System.in);
		
		while(true) {
			String inp=br.readLine();
			dout.writeUTF(inp);
			dout.flush();
			String sinp=din.readUTF();
			if(inp.equalsIgnoreCase("exit")) {
				break;
			}
			
			System.out.println("Server : "+sinp);
		}
		
		System.out.println("Disconnected");
		s.close();
		sc.close();
		
	}
}
