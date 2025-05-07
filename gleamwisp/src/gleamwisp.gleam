import gleam/erlang/process
import gleam/io
import gleam/string_tree.{from_string}
import mist
import wisp.{type Request, type Response, Text}
import wisp/wisp_mist

pub fn handle_request(_req: Request) -> Response {
  wisp.response(200)
  |> wisp.set_body(Text(from_string("hello!")))
}

pub fn main() -> Nil {
  let secret_key_base = wisp.random_string(64)

  let assert Ok(_) =
    wisp_mist.handler(handle_request, secret_key_base)
    |> mist.new()
    |> mist.port(8080)
    |> mist.start_http()

  process.sleep_forever()
}
