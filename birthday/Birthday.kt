fun Birthday(lines : List<String>) : String {
    var list = lines.toMutableList()
    
    while (!list.isEmpty()) {
        val numPeople = list[0].split(" ")[0].toInt()
        val numConn = list[0].split(" ")[1].toInt()

        if (numPeople == 0 && numConn == 0) {
            break
        }

        val connections = list.slice(1..numConn)

        testCase(numPeople, connections)


        list = list.slice(numConn+1..list.size - 1).toMutableList()

    }


    return ""
}

fun testCase(numPeople : Int, connections : List<String>) {
    println(connections)
}


fun main() {
    var lines = generateSequence(::readLine).toList()
    println(Birthday(lines))
}

