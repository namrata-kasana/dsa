object SingleNumber {
  def singleNumber(nums: Array[Int]): Int = {
    val countMap = scala.collection.mutable.HashMap[Int,Int]()

    // convert array to k,v pair
    nums.foreach (num =>
      countMap(num) = countMap.getOrElse(num, 0) + 1)

    // Use find to get the number that occurs exactly once
    countMap.find { case (k, v) => v == 1 } match {
      case Some((k, _)) => k  // Return the key if found
      case None => 0          // Return 0 if no single number is found
    }


  }
  def main(args: Array[String]): Unit = {
    // Test the singleNumber method
    val result = singleNumber(Array(1, 2, 2, 3, 3, 4, 4))
    println(s"The single number is: $result") // Should output: The single number is: 1
  }
}