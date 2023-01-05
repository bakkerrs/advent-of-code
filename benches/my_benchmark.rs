use std::vec;

use advent_of_code::*;
use criterion::{criterion_group, criterion_main, Criterion};

pub fn criterion_benchmark(c: &mut Criterion) {
    let finished_days = vec![1, 2, 3];
    for day in finished_days {
        let input = get_input(2022, day, false);
        let function_name = format!("2022 day {}, part 1", day);
        c.bench_function(&function_name, |b| b.iter(|| run_part1(2022, day, &input)));
        let function_name = format!("2022 day {}, part 2", day);
        c.bench_function(&function_name, |b| b.iter(|| run_part2(2022, day, &input)));
    }
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
