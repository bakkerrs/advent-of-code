pub fn sample_input() -> String {
    include_str!("sample/day1.txt").to_owned()
}

fn prep(input: &str) -> Vec<u32> {
    let mut elves: Vec<u32> = Vec::new();

    let mut current_cals = 0;
    for line in input.lines() {
        match line.parse::<u32>().is_ok() {
            true => current_cals += line.parse::<u32>().unwrap(),
            false => {
                elves.push(current_cals);
                current_cals = 0
            }
        }
    }
    elves.push(current_cals);
    elves
}

pub fn part1(input: &str) -> String {
    prep(input)
        .iter()
        .max()
        .expect("Could not get maximum value")
        .to_owned()
        .to_string()
}

pub fn part2(input: &str) -> String {
    let mut elves = prep(input);
    elves.sort();
    elves.reverse();
    elves.truncate(3);
    elves.iter().sum::<u32>().to_string()
}
