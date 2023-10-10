package error_Detection;
import java.util.*;
import java.io.*;

public class CRC {
	static Scanner sc=new Scanner(System.in);
	public void CRCSender() {
		System.out.println("\nSENDER SIDE");
		System.out.print("Enter the Message to Send : ");
		String message = sc.nextLine();
		
		System.out.print("Enter the generator : ");
		String generator=sc.nextLine();
		
		int data[]=new int[message.length()+generator.length()-1];
		int divisor[]=new int[generator.length()];
		
		for(int i=0;i<message.length();i++)
			data[i]=Integer.parseInt(message.charAt(i)+"");
		for(int i=0;i<generator.length();i++)
			divisor[i]=Integer.parseInt(generator.charAt(i)+"");
		
		//Calculation of CRC
		for(int i=0;i<message.length();i++)
		{
			if(data[i]==1)
				for(int j=0;j<divisor.length;j++)
					data[i+j]^=divisor[j];
		}
		
		for(int i=0;i<message.length();i++)
		{
			data[i]=Integer.parseInt(message.charAt(i)+"");
		}
		System.out.print("The Checksum code is : ");
		System.out.println(Arrays.toString(data));
		
	}
	
	public void CRCReceiver() {
		System.out.println("\nRECEIVER SIDE");
		System.out.print("Enter Checksum code : ");
		String message=sc.nextLine();
		System.out.print("Enter Generator : ");
		String generator=sc.nextLine();
		
		int data[]=new int[message.length()+generator.length()-1];
		int divisor[]=new int[generator.length()];
		
		for(int i=0;i<message.length();i++)
			data[i]=Integer.parseInt(message.charAt(i)+"");
		for(int i=0;i<generator.length();i++)
			divisor[i]=Integer.parseInt(generator.charAt(i)+"");
		
		for(int i=0;i<message.length();i++)
			if(data[i]==1)
				for(int j=0;j<divisor.length;j++)
					data[i+j]^=divisor[j];
		
		boolean flag=true;
		System.out.println("");
		for(int i=0;i<data.length;i++)
		{
			if(data[i]!=0)
			{
				System.out.println("Data is Invalid CRC error Occurred");
				flag=false;
				break;
			}
		}
		if(flag)
			System.out.println("Data is Valid");
	}
	public static void main(String[]args) {
		CRC crc=new CRC();
		crc.CRCSender();
		crc.CRCReceiver();
		
		sc.close();
	}
}
