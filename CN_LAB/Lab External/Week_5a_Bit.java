import java.util.Scanner;

/**
 * 5A_Bit_Stuffing
 */
public class Week_5a_Bit{
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        String message=sc.nextLine();
        
        int count = 0;

        for(int i=0;i<message.length();i++){
            if(message.charAt(i)=='1'){
                count++;
            }
            if(message.charAt(i)=='0'){
                count = 0;
            }
            System.out.print(message.charAt(i));
            if(count==5){
                System.out.print('0');
                count=0;
            }
        }
        sc.close();
    }
}
