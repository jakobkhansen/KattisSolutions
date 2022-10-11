use std::io::{self, BufRead};

fn main() {
    let io: io::Stdin = io::stdin();
    let mut iterator = io.lock().lines();

    let line1 = iterator.next().unwrap().unwrap();

    let nums: Vec<i64> = line1
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();

    if let &[_, a] = &nums[..2] {
        let mut ships: Vec<i64> = iterator
            .next()
            .unwrap()
            .unwrap()
            .split_whitespace()
            .map(|number| number.parse::<i64>().unwrap())
            .collect();
        ships.sort();
        let mut resources = a;
        let mut num_wins: i64 = 0;
        for ship in ships {
            if ship >= resources {
                break;
            }
            resources -= ship + 1;
            num_wins += 1;
        }
        println!("{}", num_wins);
    }
}
