package notJava;

import java.util.HashMap;
import java.util.PriorityQueue;

//interface Rankable {
///**
//* Returns the Rank of this object, using some algorithm and potentially
//* the internal state of the Rankable.
//*/
//	long getRank();
//}
//interface DataSource<K, T extends Rankable> {
//	T get (K key);
//}

public class RBC<K, T extends Rankable> {
	/**
	 * one ds for get
	 * 	hashmap
	 * 		k, t
	 * one ds for put
	 * 	-treemap or pqueue
	 * 		node (k, v)
	 * get
	 * 	if key in map
	 * 		return
	 * 	else
	 * 		get from ds
	 * 		add to map
	 * 		add to pqueue
	 * 		if size exceeds capacity
	 * 			get lowest ranked element
	 * 			remove from map and pqueue
	 * @param ds
	 * @param entriesToRetain
	 */
	HashMap<K, T> hm;
	PriorityQueue<Node> pq;
	int maxSize;
	DataSource ds;

		// Add any fields you need here
		/* Constructor with a data source (assumed to be slow) and a cache size */
		public RBC(DataSource<K,T> ds, int entriesToRetain) {
			hm = new HashMap<K, T>();
			pq = new PriorityQueue<Node>();
			this.ds = ds;
			this.maxSize = entriesToRetain;
		}

		/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
		* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
		* evicting the T with lowest rank among the ones that it has available
		* If there is a tie, the cache may choose any T with lowest rank to evict.
		*/
		public synchronized T get(K key) {
			T val = hm.get(key);
			if (val != null) {
				return val;
			} else {
				val = (T) ds.get(key);
				hm.put(key, val);
				Node n = new Node(key, val);
				pq.offer(n);
				if (hm.size() > maxSize) {
					Node lowest = pq.poll();
					hm.remove(lowest.key);
				}
				return val;
			}
		}

		class Node implements Comparable {
			K key;
			T val;
			
			public Node(K key, T val) {
				this.key = key;
				this.val = val;
			}
			@Override
			public int compareTo(Object o) {
				Node other = (Node)o;
				Long thisRank = val.getRank();
				Long otherRank = other.val.getRank();
				if (thisRank < otherRank) {
					return -1;
				} else if (thisRank > otherRank) {
					return 1;
				} else {
					return 0;
				}
			}
		}
}

