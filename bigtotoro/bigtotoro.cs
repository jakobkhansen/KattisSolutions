using System;
using System.Collections.Generic;
using System.Linq;

void Main()
{
    var lines = Enumerable.Range(0, int.MaxValue).Select(_ => Console.ReadLine()).TakeWhile(x => x != null).ToList();
    var first = lines[0]!.Split().Select(int.Parse).ToList();
    var (n, k) = (first[0], first[1]);
    var split = lines[1]!.Split();

    var acorns = lines[1]!.Split(" ", StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToList();

    var output = k;

    var counts = new int[4];
    var used = new int[4];
    List<int>[] nums = [.. Enumerable.Range(0, 4).Select(_ => new List<int>())];

    foreach (var acorn in acorns)
    {
        var mod = acorn % 4;
        counts[mod] += 1;
        nums[mod].Add(acorn);
    }

    foreach (var list in nums)
    {
        list.Sort((a, b) => b.CompareTo(a));
    }

    while (true)
    {
        var mod = output % 4;

        if (used[mod] >= nums[mod].Count)
        {
            break;
        }
        output += nums[mod][used[mod]];
        used[mod]++;
    }



    Console.WriteLine(output);
}

Main();

