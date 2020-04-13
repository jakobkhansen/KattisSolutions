fun Divisible(lines : List<String>) : String {
    val numTestCases = lines[0].split(" ")[0].toLong()
    var retString = ""
    var leftIndex = 1



    for (i in 1..numTestCases) {
        val d = lines[leftIndex].split(" ")[0].toLong()
        leftIndex++
        val array = lines[leftIndex].split(" ").map { it.toLong() }
        val sums = precompute(array)
        retString += bruteForce(array, sums, d).toString() + "\n"
        leftIndex++
    }
    return retString.trim()
}

fun precompute(array : List<Long>) : List<Long> {
    var count = 0L
    val sums = mutableListOf<Long>()
    for (i in array) {
        count += i
        sums.add(count)
    }

    return sums
}

fun bruteForce(array : List<Long>, sums : List<Long>, d : Long) : Long {

    var count = 0L
    for (i in 0..array.size) {
        for (j in i..array.size - 1) {
            var sum : Long
            if (i > 0) {
                sum = sums[j] - sums[i - 1]
            } else {
                sum = sums[j]
            }

            if (sum % d == 0L) {
                count++
            }
        }
    }


    return count
}


fun main() {
    var lines = generateSequence(::readLine).toList()
    println(Divisible(lines))
}

