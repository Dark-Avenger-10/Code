package csma;

public class CD extends Thread{
	public int totalCollisions=0;
	public int failures=0;
	public int state=0;
	
	private String name;
	private int countCollisions;
	private int nPackets;
	private int delay;
	private long time=0;
	
	public CD(String name,int nPackets,int delay) {
		this.name=name;
		this.nPackets=nPackets;
		this.delay=delay;
		
		System.out.println("New Host : ");
		System.out.println("Name : "+name);
		System.out.println("No.of Packets to Transmitt : "+nPackets);
		System.out.println("Delay : "+delay);
	}
	
	void getChrorno() {
		time=java.lang.System.currentTimeMillis();
	}
	
	void stopChrono() {
		long time2=java.lang.System.currentTimeMillis();
		time=time2-time;
		System.out.println(name+ "Time delay : "+time+"ms");
	}
	
	public void run() {
		for(int packet=1;packet<=nPackets;packet++) {
			countCollisions=0;
			while(countCollisions<10) {
				if(state==0) {
					System.out.println("The host "+ name+ "Is not Idle");
					try {
						Thread.sleep(delay);
					}
					catch{
						sy
					}
				}
			}
		}
	}
	

}
