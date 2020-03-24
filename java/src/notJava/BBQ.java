package notJava;

import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
interface MultiPutBlockingBoundedQueue {
/*
* Sets the capacity of the buffer. Can be called only once.
* If called more than once or if the passed capacity is <= 0,
* throw an exception.
*/
public void init(int capacity) throws Exception;
/*
* Get the next item from the queue
* throws Exception if not initialized
*/
public Object get() throws Exception;
/*
 * Put the item to the tail of the queue.
 * throws Exception if not initialized
 */

public void put(Object obj) throws Exception;
 /*
 * Put the list of items in sequence without mixing
 * with items from other put or multiput calls.
 * The list can be more than the capacity
 * throws Exception if not initialized
 */

public void multiput(List<Object> objs) throws Exception;
}

public class BBQ implements MultiPutBlockingBoundedQueue{
	boolean inited = false;
	Lock lock;
	Lock wlock;
	Condition notFull;
	Condition notEmpty;
	int capacity;
	LinkedList<Object> q;
	/*
	* threadSafe bounded blocking queue implementation.
	* Expected to be used in a Producer­>Consumer pattern
	*/


	@Override
	public void init(int capacity) throws Exception {
		this.capacity = capacity;
		this.q = new LinkedList<Object>();
		this.lock = new ReentrantLock();
		this.wlock = new ReentrantLock();
		this.notEmpty = this.lock.newCondition();
		this.notFull = this.lock.newCondition();
		this.inited = true;
		
	}

	@Override
	public Object get() throws Exception {
		try {
			this.lock.lock();
			while (this.q.size() == 0) {
				this.notEmpty.await();
			}
			Object val = this.q.poll();
			this.notFull.signalAll();
			return val;
		} catch (Exception e){
			e.printStackTrace();
			return null;
		}
			finally {
			this.lock.unlock();
		}
	}

	@Override
	public void put(Object obj) throws Exception {
		try {
			this.wlock.lock();
			this.lock.lock();
			if (this.q.size() == capacity) {
				this.notFull.await();
			}
			this.q.push(obj);
			this.notEmpty.signalAll();
		} finally {
			this.wlock.unlock();
			this.lock.unlock();
		}
	}
	
	@Override
	public void multiput(List<Object> objs) throws Exception {
		try {
			this.wlock.lock();
			this.lock.lock();
			for (Object o : objs) {
				while (this.q.size() == capacity) {
					this.notFull.await();
				}
				this.put(o);
				this.notEmpty.signalAll();
			}
		} finally {
			this.wlock.unlock();
			this.lock.unlock();
		}
	}

}
