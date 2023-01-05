mod input_helper;
mod y2022;

pub fn get_input(_year: u16, day: u8, sample: bool) -> String {
    let sample_input = y2022::get_sample_input(day);
    match sample {
        true => sample_input(),
        false => input_helper::load_input(2022, day),
    }
}

pub fn run_part1(_year: u16, day: u8, input: &str) -> String {
    let part1 = y2022::get_part1(day);
    part1(&input)
}

pub fn run_part2(_year: u16, day: u8, input: &str) -> String {
    let part2 = y2022::get_part2(day);
    part2(&input)
}

pub fn run(year: u16, day: u8, part: u8, sample: bool) {
    let input = get_input(year, day, sample);

    match part {
        0 => println!(
            "{} day {} - part 1: {} | part 2: {}",
            year,
            day,
            run_part1(year, day, &input),
            run_part2(year, day, &input)
        ),
        1 => println!(
            "{} day {} - part 1: {}",
            year,
            day,
            run_part1(year, day, &input)
        ),
        2 => println!(
            "{} day {} - part 2: {}",
            year,
            day,
            run_part2(year, day, &input)
        ),
        _ => println!("That partnumber does not exist."),
    }
}
