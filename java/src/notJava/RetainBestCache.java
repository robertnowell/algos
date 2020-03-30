package notJava;

import java.util.PriorityQueue;
import java.util.TreeMap;

/**
 * 	Followup questions:
	If a Rankable's rank is defined as it's last access time, the retain-best cache becomes an LRU cache.
	If the candidate doesn't know the 'standard' map + list LRU solution, ask them to re-implement the retain-best cache to take advantage of knowing what
	the Rank function is
	If the candidate does know the standard LRU solution, ask them to contrast the performance of their retain-best cache to the standard LRU
	(Hardmode) How would you need to enhance your solution to handle Rankables that frequently changed Rank?
	LRU is the first step of this - Objects increase in rank each time they are accessed. Another variant might be Most/Least Frequently Used, where rank
	increases or decreases by one each access
	If you had a cache of a graph that traversals were happening on, you could declare a rank based on where the traversal was at the moment, and so
	ranks could change without being accessed (rank would be a function of how close to the traversal front the node was). In the worst case, this could
	trigger a full re-rank of the cache on each cache miss.	
 */
interface Rankable {
	/**
	* Returns the Rank of this object, using some algorithm and potentially
	
	5/23/2019 Retain-Best Cache - Unite - LinkedIn Corporate Wiki
	
	https://iwww.corp.linkedin.com/wiki/cf/display/Unite/Retain-Best+Cache 2/11
	To begin with, assume that ranks will not change once read. Don't offer this information until the candidate asks.

	Sample TreeMap Solution:
	* the internal state of the Rankable.
	*/
	long getRank();
}

interface DataSource<K, T extends Rankable> {
	T get (K key);
}

public class RetainBestCache<K, T extends Rankable> {
	TreeMap<K, T> map;
	int size;
	int maxSize;
	K minKey;
	T minVal;
	DataSource data;

	// Add any fields you need here
	/* Constructor with a data source (assumed to be slow) and a cache size */
	public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
		this.map = new TreeMap<K, T>();
		this.size = 0;
		this.maxSize = entriesToRetain;
		this.data = ds;
	}
	/* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
	* retrieves it from the data source. If the cache is full, attempt to cache the returned data,
	* evicting the T with lowest rank among the ones that it has available
	* If there is a tie, the cache may choose any T with lowest rank to evict.
	*/
	public T get(K key) {
		T val = map.get(key);
		if (val == null) {
			val = (T) this.data.get(key);
			if (this.size < this.maxSize) {
				map.put(key, val);
				if (this.minKey == null) {
					this.minKey = key;
					this.minVal = val;
				}
				this.size++;
			} else {
				if (this.min.getRank() < val.getRank()) {
					this.map.remove()
				}
			}
		} else {
			return val;
		}
	}
}
