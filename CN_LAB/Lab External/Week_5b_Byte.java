import java.util.Scanner;
import java.util.StringTokenizer;
public class Week_5b_Byte{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Message : ");
        String message=sc.nextLine();
        StringTokenizer st = new StringTokenizer(message," ");

        System.out.print("\nDLE STX ");
        while(st.hasMoreTokens()) {
            Boolean flag=false;
            String msg=st.nextToken();
            int i=0;
            for(i=0;i<msg.length()-2;i++){
                System.out.print(msg.charAt(i));
                String temp="";
                temp=temp + msg.charAt(i) + msg.charAt(i+1) + msg.charAt(i+2);
                //System.out.println("Data in temp : " + temp);
                if(temp.equals("DLE")){
                    flag=true;
                    break;
                }
            }
            if(flag){
                i++;
            }
            while(i<msg.length()){
                System.out.print(msg.charAt(i));
                i++;
            }
            if(flag){
                System.out.print("DLE");
            }
            
            
            System.out.print(" ");
        }
        System.out.print("DLE ETX");
        sc.close();
    }
}