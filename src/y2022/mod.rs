mod day1;
mod day2;
mod day3;

pub fn get_part1(day: u8) -> fn(input: &str) -> String {
    match day {
        1 => day1::part1,
        2 => day2::part1,
        3 => day3::part1,
        _ => panic!(),
    }
}
pub fn get_part2(day: u8) -> fn(input: &str) -> String {
    match day {
        1 => day1::part2,
        2 => day2::part2,
        3 => day3::part2,
        _ => panic!(),
    }
}

pub fn get_sample_input(day: u8) -> fn() -> String {
    match day {
        1 => day1::sample_input,
        2 => day2::sample_input,
        3 => day3::sample_input,
        _ => panic!(),
    }
}
