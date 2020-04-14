fun Mali(lines : MutableList<String>) : String {
    var min_a = -1
    var min_b = -1
    var max_a = 0
    var max_b = 0

    lines.removeAt(0)

    var retString = ""

    lines.forEach { line ->
        val nums = line.split(" ").map { it.toInt() }

        if (min_a == -1 || min_a > nums[0]) {
            min_a = nums[0]
        }

        if (min_b == -1 || min_b > nums[1]) {
            min_b = nums[1]
        }

        if (max_a < nums[0]) {
            max_a = nums[0]
        }

        if (max_b < nums[1]) {
            max_b = nums[1]
        }


        val pot1 = min_a + max_b
        val pot2 = max_a + min_b

        if (pot1 > pot2) {
            retString += pot1.toString() + "\n"
        } else {
            retString += pot2.toString() + "\n"
        }

    }
    return retString.trim()
}


fun main() {
    val lines = generateSequence(::readLine).toMutableList()
    println(Mali(lines))
}

