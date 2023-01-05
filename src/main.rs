use clap::Parser;

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
pub struct Args {
    /// Advent of code year to run code for
    #[arg(short, long, default_value_t = 2022)]
    year: u16,

    /// Day to run
    #[arg(short, long, default_value_t = 1)]
    day: u8,

    /// Part to run, default both
    #[arg(short, long, default_value_t = 0)]
    part: u8,

    /// Use sample input
    #[arg(short, long, default_value_t = false)]
    sample: bool,
}

fn main() {
    let args = Args::parse();
    advent_of_code::run(args.year, args.day, args.part, args.sample);
}
