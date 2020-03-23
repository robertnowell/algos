package bbq;

import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

interface MultiPutBlockingBoundedQueue {
	public void init(int capacity) throws Exception;
	public Object get() throws Exception;
	public void put(Object obj) throws Exception;
	public <T> void multiput(List<Object> objs) throws Exception;
}

public class BBQ implements MultiPutBlockingBoundedQueue{
	private boolean initialized = false;
	private int capacity;
	public LinkedList<Object> q;
	private Condition notEmpty;
	private Condition notFull;
	private Lock lock;
	private Lock wlock;
	@Override
	public void init(int capacity) throws Exception {
		this.q = new LinkedList<Object>();
		this.capacity = capacity;
		this.initialized = true;
		this.lock = new ReentrantLock();
		this.wlock = new ReentrantLock();
		this.notEmpty = this.lock.newCondition();
		this.notFull = this.lock.newCondition();
//		this.lock.lock();
//		this.notFull.signal();
//		this.lock.unlock();
	}

	@Override
	public Object get() throws Exception {
		try{
			printLockState();

			lock.lock();
			printLockState();
			if (!this.initialized) {
				throw new Exception("uninitialized get");
			}
			while (this.q.size() == 0) {
//				System.out.println("waiting until q not full");
				notEmpty.await();
//				System.out.println("confirmed q not full");
			}
			if (this.q.size() == 0) {
				throw new Exception("cannot get an empty queue");
			}
			notFull.signalAll();
			return q.poll();
		} catch (Exception e){
			e.printStackTrace();
			throw (e);
		}
		finally {
			lock.unlock();
		}
	}
	
	public void printLockState() {
		System.out.println(Thread.currentThread() +", wlock: " + wlock.toString());
		System.out.println(Thread.currentThread() +", lock: " + lock.toString());
	}

	@Override
	public void put(Object obj) throws Exception {
		try{
			// order matters because 
			wlock.lock();
			lock.lock();
//			printLockState();

			if (!this.initialized) {
				throw new Exception("uninitialized put");
			}
			while (this.q.size() == this.capacity) {
					System.out.println(Thread.currentThread() + "waiting until q not full");
					notFull.await();
					System.out.println(Thread.currentThread() + "confirmed q not full");			
			}
			
			if (this.q.size() >= this.capacity) {
				throw new Exception("put exceeds capacity. size: " + this.q.size() + ", " + obj);
			}
			q.add(obj);
			notEmpty.signalAll();
		} catch (Exception e){
			e.printStackTrace();
			throw (e);
		}
		finally {
			System.out.println(this.q);

			System.out.println(Thread.currentThread() + " unlocking");
			wlock.unlock();
			lock.unlock();
			System.out.println(Thread.currentThread() + " unlocked");
			printLockState();

		}
	}

	@Override
	public <T> void multiput(List<Object> objs) throws Exception {
		try{
			// order matters because 
			wlock.lock();
			lock.lock();
//			printLockState();

			if (!this.initialized) {
				throw new Exception("uninitialized put");
			}
			for (Object o : objs) {
				while (this.q.size() == this.capacity) {
					System.out.println(Thread.currentThread() + "multiput waiting until q not full");
					notFull.await();
					System.out.println(Thread.currentThread() + "confirmed q not full");			
				}
				this.put(o);
				notEmpty.signalAll();
			}
		} catch (Exception e){
			e.printStackTrace();
			throw (e);
		}
		finally {
			System.out.println(this.q);

			System.out.println(Thread.currentThread() + " unlocking");
			wlock.unlock();
			lock.unlock();
			System.out.println(Thread.currentThread() + " unlocked");
			printLockState();

		}
	}

}
