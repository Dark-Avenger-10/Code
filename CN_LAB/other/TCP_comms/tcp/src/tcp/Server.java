package tcp;
import java.io.*;
import java.net.*;
public class Server {
	public static void main(String[]args) throws IOException {
		ServerSocket ss=new ServerSocket(3000);
		Socket s=ss.accept();
		System.out.println("Client Connected");
		
		DataOutputStream dout=new DataOutputStream(s.getOutputStream());
		DataInputStream din=new DataInputStream(s.getInputStream());
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		while(true) {
			String clinp=din.readUTF();
			System.out.println("Client : "+clinp);
			
			if(clinp.equalsIgnoreCase("exit")) {
				break;
			}
			
			String ut=br.readLine();
			dout.writeUTF(ut);
			
			if(ut.equalsIgnoreCase("exit")) {
				break;
			}
		}
		ss.close();
	}
}
