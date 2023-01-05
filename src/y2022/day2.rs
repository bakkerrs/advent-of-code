use core::panic;

pub fn sample_input() -> String {
    include_str!("sample/day2.txt").to_owned()
}

pub fn part1(input: &str) -> String {
    let mut scores: Vec<i8> = Vec::new();

    for line in input.lines() {
        let args = line.chars().collect::<Vec<char>>();
        let opponent = args[0] as i8 - 65;
        let player = args[2] as i8 - 88;

        let result_score = match (&player - &opponent).rem_euclid(3) {
            0 => 3,
            1 => 6,
            2 => 0,
            _ => panic!(""), // modulo should ensure this never happens
        };

        scores.push(player + result_score + 1);
    }

    scores.iter().sum::<i8>().to_string()
}

pub fn part2(input: &str) -> String {
    let mut scores: Vec<i8> = Vec::new();

    for line in input.lines() {
        let args = line.chars().collect::<Vec<char>>();
        let opponent = args[0] as i8 - 65;
        let result = args[2] as i8 - 88;

        let player = (&opponent + &result - 1).rem_euclid(3);

        let result_score = match result {
            0 => 0,
            1 => 3,
            2 => 6,
            _ => panic!(""), // modulo should ensure this never happens
        };

        scores.push(player + result_score + 1);
    }

    scores.iter().sum::<i8>().to_string()
}
