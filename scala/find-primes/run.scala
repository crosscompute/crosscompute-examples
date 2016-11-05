object FindPrimeNumbers {

  val usage =
    """
      Usage: scala findprime.scala [arg1: number of primes]
    """.stripMargin

  def main (args: Array[String]) {
    if(args.length == 0) println(usage)

    try {

      val integerArg  = args.head.toInt
      val primeFactorsList = factors(integerArg)
      println(s"prime_factors = ${primeFactorsList}")
      println(s"unique_factor_count = ${primeFactorsList.length} ")

    }
    catch {
      case e: NumberFormatException => println(s"Your argument ${e} is not an Integer")
      case e: Throwable => println(e.getMessage)

    }

  }

  // borrowed from http://louisbotterill.blogspot.com/2009/03/prime-factorization-comparison-between.html
  def factors(n:Int):List[Int] = {
    def divides(d:Int, n:Int) = (n % d) == 0
    def ld(n:Int):Int =  ldf(2, n)
    def ldf(k:Int, n:Int):Int = {
      if (divides(k, n)) k
      else if ((k*k) > n) n
      else ldf((k+1), n)
    }
    n match {
      case 1 => Nil
      case _ => val p = ld(n); p :: factors(n / p)
    }
  }
}
