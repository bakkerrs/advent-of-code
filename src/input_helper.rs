use isahc::cookies::{Cookie, CookieJar};
use isahc::http::{StatusCode, Uri};
use isahc::{prelude::*, Request};
use std::fs::{self, File};
use std::io::Write;
use std::path::Path;

pub fn load_input(year: u16, day: u8) -> String {
    let file_path = format!("input/{}/day{}.txt", year, day);
    let input_path = Path::new(&file_path);
    match input_path.exists() {
        true => fs::read_to_string(input_path).expect("Could not read cached input file"),
        false => get_from_aoc(year, day),
    }
}

fn get_from_aoc(year: u16, day: u8) -> String {
    let aoc_cookie = Cookie::builder("session", "53616c7465645f5fe8e369cbe5e98818b89f23ce1b68c9fa63dec4cb33dc8693f43a04c714cb79eee582c296dfa4de644342954243fd0a42ae39ca57236e92e2")
    .domain("adventofcode.com").path("/").secure(true).build().unwrap();

    let request_path = format!("https://adventofcode.com/{}/day/{}/input", year, day);
    let request_uri = request_path.parse::<Uri>().unwrap();

    let cookie_jar = CookieJar::new();
    cookie_jar.set(aoc_cookie, &request_uri).unwrap();

    let request = Request::builder()
        .uri(request_uri)
        .cookie_jar(cookie_jar)
        .header(
            "User-Agent",
            "github/rsbakker/advent-of-code by robin@rsbnet.eu",
        );

    let mut response = request.body(()).unwrap().send().unwrap();
    let input = match response.status() {
        StatusCode::OK => response.text().unwrap(),
        _ => panic!("Unable to get input file"),
    };

    let file_path = format!("input/{}/day{}.txt", year, day);

    let mut file = File::create(&file_path).unwrap();
    file.write(&input.as_bytes()).unwrap();
    input
}
