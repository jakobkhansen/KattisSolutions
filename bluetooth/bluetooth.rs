use std::io::{self, BufRead};

fn main() {
    let io: io::Stdin = io::stdin();
    let mut line_iter = io.lock().lines();
    let _: i32 = line_iter.next().unwrap().unwrap().parse().unwrap();

    let mut left_blue = 0;
    let mut right_blue = 0;

    let mut left_top_bad = 0;
    let mut left_bottom_bad = 0;

    let mut right_top_bad = 0;
    let mut right_bottom_bad = 0;

    line_iter.for_each(|line_res| {
        let line = line_res.unwrap();
        let mut line_split = line.split_whitespace();
        let num_string = line_split.next().unwrap();
        let condition = line_split.next().unwrap();
        let blue = match condition.chars().nth(0).unwrap() {
            'b' => 1,
            _ => 0,
        };
        let missing = match condition.chars().nth(0).unwrap() {
            'm' => 1,
            _ => 0,
        };

        // Left side
        match num_string.chars().nth(0).unwrap() {
            // Top
            '+' => {
                left_top_bad += missing;
                left_blue += blue;
            }

            // Bottom
            '-' => {
                left_bottom_bad += missing;
                left_blue += blue;
            }
            _ => {}
        }

        match num_string.chars().nth(1).unwrap() {
            // Top
            '+' => {
                right_top_bad += missing;
                right_blue += blue;
            }

            // Bottom
            '-' => {
                right_bottom_bad += missing;
                right_blue += blue;
            }
            _ => {}
        }
    });
    let mut result = 0;
    if left_blue > 0 || (left_bottom_bad >= 8 || left_top_bad >= 8) {
        result += 1;
        if right_blue > 0 || (right_bottom_bad >= 8 || right_top_bad >= 8) {
            result += 1;
        }
    }
    println!("{}", result)
}
