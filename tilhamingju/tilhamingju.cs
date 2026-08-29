using System;
using System.Linq;

void Main()
{
    var lines = Enumerable.Range(0, int.MaxValue).Select(_ => Console.ReadLine()).TakeWhile(x => x != null).ToList();
    Console.WriteLine("TIL HAMINGJU MED AFMAELID FORRITUNARKEPPNI FRAMHALDSSKOLANNA!");
}

Main();
