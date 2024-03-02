import java.util.concurrent.Semaphore;
import java.util.Random;

class NarrowRoad {
	private int maxCars;
	private int currentCars;
	private Semaphore leftGate;
	private Semaphore rightGate;
	private int leftCars;
	private int rightCars;
	private Random random;

	public NarrowRoad(int maxCars) {
		this.maxCars = maxCars;
		this.currentCars = 0;
		this.leftGate = new Semaphore(1);
		this.rightGate = new Semaphore(0);
		this.leftCars = 20;
		this.rightCars = 20;
		this.random = new Random();
	}

	public void leftGatekeeper() throws InterruptedException {
		while (true) {
			if (this.leftGate.tryAcquire()) {
				while (this.currentCars < this.maxCars && this.leftCars > 0) {
					this.currentCars++;
					this.leftCars--;
					System.out.println("   Car from left gate entered. Current cars: " + this.currentCars);
					Thread.sleep(1000);
				}
				if (this.currentCars == this.maxCars) 
					System.out.println("   Left gate allow maximum number of cars. Turning to right gate to open...");
				if (this.leftCars == 0) 
					System.out.println("   No more cars from left side. Turning to right gate to open...");

				this.rightGate.release();
				this.currentCars = 0;
				Thread.sleep(3000); 
			}
		}
	}

	public void rightGatekeeper() throws InterruptedException {
		while (true) {
			if (this.rightGate.tryAcquire()) {
				while (this.currentCars < this.maxCars && this.rightCars > 0) {
					this.currentCars++;
					this.rightCars--;
					System.out.println("   Car from right gate entered. Current cars: " + this.currentCars);
					Thread.sleep(1000);
				}
				if (this.currentCars == this.maxCars) 
					System.out.println("   Right gate allow maximum number of cars. Turning to left gate to open...");
				
				if (this.rightCars == 0) 
					System.out.println("   No more cars from right side. Turning to left gate to open...");
				
				this.leftGate.release();
				this.currentCars = 0;
				Thread.sleep(3000);
			}
		}
	}

	public void leftCar() throws InterruptedException {
		while (true) {
			Thread.sleep((random.nextInt(10) + 1)*1000);
			this.leftCars++;
			System.out.println("Car from left side arrived. Number of cars: " + this.leftCars);
		}
	}

	public void rightCar() throws InterruptedException {
		while (true) {
			Thread.sleep((random.nextInt(10) + 1)*1000);
			this.rightCars++;
			System.out.println("Car from right side arrived. Number of cars: " + this.rightCars);
		}
	}

	public static void main(String[] args) {
		NarrowRoad road = new NarrowRoad(5);
		new Thread(() -> {
			try {
				road.leftGatekeeper();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}).start();
		new Thread(() -> {
			try {
				road.rightGatekeeper();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}).start();
		new Thread(() -> {
			try {
				road.leftCar();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}).start();
		new Thread(() -> {
			try {
				road.rightCar();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}).start();
	}
}