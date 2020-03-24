package notJava;

import java.util.List;

public class DepthSum {
	public int depthHelper(List<NestedInteger> input, int depth) {
		int sum = 0;
		for (NestedInteger ni : input) {
			if (ni.isInteger()) {
				sum += ni.getInteger() * depth;
			} else {
				sum += depthHelper(ni.getList(), depth+1);
			}
		}
		return sum;
		
	}
	/**
	* Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
	* For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
	* Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
	*/
	public int depthSum (List<NestedInteger> input)
	{
		return depthHelper(input, 1);
		// for reach elem in list
		// if elem is an integer, add int to sum
		// if elem is a list, recurse
		// return sum
	}
	
	/**
	* This is the interface that represents nested lists.
	* You should not implement it, or speculate about its implementation.
	*/
	public interface NestedInteger	{
		
		/** @return true if this NestedInteger holds a single integer, rather than a nested list */
		boolean isInteger();
		/** @return the single integer that this NestedInteger holds, if it holds a single integer
		* Return null if this NestedInteger holds a nested list */
		
		Integer getInteger();
		
		/** @return the nested list that this NestedInteger holds, if it holds a nested list
		* Return null if this NestedInteger holds a single integer */
		List<NestedInteger> getList();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
