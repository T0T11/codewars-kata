def multiTable(n: Int): String = 
  val nums = (1 to 10).toList
  val m = for i <- nums yield s"$i * $n = ${i * n}" 
  m.mkString("\n")
