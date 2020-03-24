package notJava;

import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.CountDownLatch;

public class Runner {
	public BBQ bbq;
	public CountDownLatch latch;
	private class PutWorker implements Runnable {
		int mult;
		public PutWorker(int mult) {
			this.mult = mult;
		}
		@Override
		public void run() {
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 1000000; j++) {
					if (j == 0) {
						try {
//							System.out.println(Thread.currentThread() + " attempting to put " + i);
							bbq.put(10*mult+i);
							System.out.println(Thread.currentThread() + " successfully put  " + i);
						} catch (Exception e) {
							e.printStackTrace();
						}
					}
				}
			}
			latch.countDown();
		}
	}
	private class MultiPutWorker implements Runnable {
		int mult;
		public MultiPutWorker(int mult) {
			this.mult = mult;
		}
		@Override
		public void run() {
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 1000000; j++) {
					if (j == 0) {
						try {
//							System.out.println(Thread.currentThread() + " attempting to put " + i);
							List<Object> l = new LinkedList<Object>();
							for (int q = 1000*mult+i; q < 1000*mult+i+10; q++) {
								l.add(q);
								System.out.println(Thread.currentThread() + " multiput  " + i);

							}
							bbq.multiput(l);
//							System.out.println(Thread.currentThread() + " successfully put  " + l);
						} catch (Exception e) {
							e.printStackTrace();
						}
					}
				}
			}
			latch.countDown();
		}
	}	
	private class GetWorker implements Runnable {

		@Override
		public void run() {
			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 1000000; j++) {
					if (j == 0) {
						try {
							System.out.println(Thread.currentThread() + " attempting to get");
							int val = (int) bbq.get();
//							System.out.println(Thread.currentThread() + " got value " + val);
						} catch (Exception e) {
							e.printStackTrace();
						}
					}
				}
			}
			latch.countDown();
		}
	}

	public static void main(String[] args) {
		int numThreads = 30;

		Runner r = new Runner();
		r.latch = new CountDownLatch(numThreads);
		r.bbq = new BBQ();
		try {
			r.bbq.init(10);
		} catch (Exception e) {
			e.printStackTrace();
		}
		for (int i = 0; i < 66; i++) {
			Thread t = new Thread(r.new GetWorker());
			t.start();
		}
		for (int i = 0; i < numThreads; i++) {
			Thread t = new Thread(r.new PutWorker(i));
			t.start();
		}
		for (int i = 0; i < numThreads; i++) {
			Thread t = new Thread(r.new MultiPutWorker(i));
			t.start();
		}
//		System.out.println("***************************************" + r.totalPut);
		try {
			r.latch.await();
			System.out.println("done");

		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
