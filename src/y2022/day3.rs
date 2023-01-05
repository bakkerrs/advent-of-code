pub fn sample_input() -> String {
    include_str!("sample/day3.txt").to_owned()
}

pub fn part1(input: &str) -> String {
    let ascii: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .chars()
        .collect();
    let mut priorities: Vec<usize> = Vec::new();

    for line in input.lines() {
        let half_length = line.len() / 2;
        let first_half = &line[0..half_length];
        let second_half = &line[half_length..];
        for char in first_half.chars() {
            if second_half.contains(char) {
                priorities.push(ascii.iter().position(|x| x == &char).unwrap_or(99) + 1);
                break;
            }
        }
    }

    priorities.iter().sum::<usize>().to_string()
}

pub fn part2(input: &str) -> String {
    let ascii: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .chars()
        .collect();
    let mut priorities: Vec<usize> = Vec::new();

    let mut current_elf = 0;
    let mut common: Vec<char> = Vec::new();
    for line in input.lines() {
        if current_elf % 3 == 0 {
            common = line.chars().collect();
        } else if current_elf % 3 == 1 {
            let mut new_common: Vec<char> = Vec::new();
            for char in line.chars() {
                if common.contains(&char) {
                    new_common.push(char)
                }
            }
            common = new_common;
        } else if current_elf % 3 == 2 {
            for char in line.chars() {
                if common.contains(&char) {
                    priorities.push(ascii.iter().position(|x| x == &char).unwrap_or(99) + 1);
                    break;
                }
            }
        }

        current_elf += 1;
    }
    priorities.iter().sum::<usize>().to_string()
}
