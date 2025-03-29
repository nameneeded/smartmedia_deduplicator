# Project structure as of 2025-03-29 01:42:13

```text
.
├── .env.example
├── .flash
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── behave
│   │   ├── black
│   │   ├── blackd
│   │   ├── distro
│   │   ├── fastapi
│   │   ├── httpx
│   │   ├── identify-cli
│   │   ├── isort
│   │   ├── isort-identify-imports
│   │   ├── nodeenv
│   │   ├── normalizer
│   │   ├── openai
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.12
│   │   ├── pre-commit
│   │   ├── py.test
│   │   ├── pytest
│   │   ├── python
│   │   ├── python3
│   │   ├── python3.12
│   │   ├── tqdm
│   │   ├── uvicorn
│   │   └── virtualenv
│   ├── include
│   │   └── python3.12
│   ├── lib
│   │   └── python3.12
│   │       └── site-packages
│   │           ├── 30fcd23745efe32ce681__mypyc.cpython-312-darwin.so
│   │           ├── PyYAML-6.0.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── _black_version.py
│   │           ├── _pytest
│   │           │   ├── __init__.py
│   │           │   ├── _argcomplete.py
│   │           │   ├── _code
│   │           │   │   ├── __init__.py
│   │           │   │   ├── code.py
│   │           │   │   └── source.py
│   │           │   ├── _io
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pprint.py
│   │           │   │   ├── saferepr.py
│   │           │   │   ├── terminalwriter.py
│   │           │   │   └── wcwidth.py
│   │           │   ├── _py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── error.py
│   │           │   │   └── path.py
│   │           │   ├── _version.py
│   │           │   ├── assertion
│   │           │   │   ├── __init__.py
│   │           │   │   ├── rewrite.py
│   │           │   │   ├── truncate.py
│   │           │   │   └── util.py
│   │           │   ├── cacheprovider.py
│   │           │   ├── capture.py
│   │           │   ├── compat.py
│   │           │   ├── config
│   │           │   │   ├── __init__.py
│   │           │   │   ├── argparsing.py
│   │           │   │   ├── compat.py
│   │           │   │   ├── exceptions.py
│   │           │   │   └── findpaths.py
│   │           │   ├── debugging.py
│   │           │   ├── deprecated.py
│   │           │   ├── doctest.py
│   │           │   ├── faulthandler.py
│   │           │   ├── fixtures.py
│   │           │   ├── freeze_support.py
│   │           │   ├── helpconfig.py
│   │           │   ├── hookspec.py
│   │           │   ├── junitxml.py
│   │           │   ├── legacypath.py
│   │           │   ├── logging.py
│   │           │   ├── main.py
│   │           │   ├── mark
│   │           │   │   ├── __init__.py
│   │           │   │   ├── expression.py
│   │           │   │   └── structures.py
│   │           │   ├── monkeypatch.py
│   │           │   ├── nodes.py
│   │           │   ├── outcomes.py
│   │           │   ├── pastebin.py
│   │           │   ├── pathlib.py
│   │           │   ├── py.typed
│   │           │   ├── pytester.py
│   │           │   ├── pytester_assertions.py
│   │           │   ├── python.py
│   │           │   ├── python_api.py
│   │           │   ├── python_path.py
│   │           │   ├── recwarn.py
│   │           │   ├── reports.py
│   │           │   ├── runner.py
│   │           │   ├── scope.py
│   │           │   ├── setuponly.py
│   │           │   ├── setupplan.py
│   │           │   ├── skipping.py
│   │           │   ├── stash.py
│   │           │   ├── stepwise.py
│   │           │   ├── terminal.py
│   │           │   ├── threadexception.py
│   │           │   ├── timing.py
│   │           │   ├── tmpdir.py
│   │           │   ├── unittest.py
│   │           │   ├── unraisableexception.py
│   │           │   ├── warning_types.py
│   │           │   └── warnings.py
│   │           ├── _yaml
│   │           │   └── __init__.py
│   │           ├── annotated_types
│   │           │   ├── __init__.py
│   │           │   ├── py.typed
│   │           │   └── test_cases.py
│   │           ├── annotated_types-0.7.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── anyio
│   │           │   ├── __init__.py
│   │           │   ├── _backends
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _asyncio.py
│   │           │   │   └── _trio.py
│   │           │   ├── _core
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _asyncio_selector_thread.py
│   │           │   │   ├── _eventloop.py
│   │           │   │   ├── _exceptions.py
│   │           │   │   ├── _fileio.py
│   │           │   │   ├── _resources.py
│   │           │   │   ├── _signals.py
│   │           │   │   ├── _sockets.py
│   │           │   │   ├── _streams.py
│   │           │   │   ├── _subprocesses.py
│   │           │   │   ├── _synchronization.py
│   │           │   │   ├── _tasks.py
│   │           │   │   ├── _tempfile.py
│   │           │   │   ├── _testing.py
│   │           │   │   └── _typedattr.py
│   │           │   ├── abc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _eventloop.py
│   │           │   │   ├── _resources.py
│   │           │   │   ├── _sockets.py
│   │           │   │   ├── _streams.py
│   │           │   │   ├── _subprocesses.py
│   │           │   │   ├── _tasks.py
│   │           │   │   └── _testing.py
│   │           │   ├── from_thread.py
│   │           │   ├── lowlevel.py
│   │           │   ├── py.typed
│   │           │   ├── pytest_plugin.py
│   │           │   ├── streams
│   │           │   │   ├── __init__.py
│   │           │   │   ├── buffered.py
│   │           │   │   ├── file.py
│   │           │   │   ├── memory.py
│   │           │   │   ├── stapled.py
│   │           │   │   ├── text.py
│   │           │   │   └── tls.py
│   │           │   ├── to_interpreter.py
│   │           │   ├── to_process.py
│   │           │   └── to_thread.py
│   │           ├── anyio-4.9.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── behave
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _stepimport.py
│   │           │   ├── _types.py
│   │           │   ├── api
│   │           │   │   ├── __init__.py
│   │           │   │   └── async_step.py
│   │           │   ├── capture.py
│   │           │   ├── compat
│   │           │   │   ├── __init__.py
│   │           │   │   └── collections.py
│   │           │   ├── configuration.py
│   │           │   ├── contrib
│   │           │   │   ├── __init__.py
│   │           │   │   ├── formatter_missing_steps.py
│   │           │   │   ├── scenario_autoretry.py
│   │           │   │   └── substep_dirs.py
│   │           │   ├── fixture.py
│   │           │   ├── formatter
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _builtins.py
│   │           │   │   ├── _registry.py
│   │           │   │   ├── ansi_escapes.py
│   │           │   │   ├── base.py
│   │           │   │   ├── formatters.py
│   │           │   │   ├── json.py
│   │           │   │   ├── null.py
│   │           │   │   ├── plain.py
│   │           │   │   ├── pretty.py
│   │           │   │   ├── progress.py
│   │           │   │   ├── rerun.py
│   │           │   │   ├── sphinx_steps.py
│   │           │   │   ├── sphinx_util.py
│   │           │   │   ├── steps.py
│   │           │   │   └── tags.py
│   │           │   ├── i18n.py
│   │           │   ├── importer.py
│   │           │   ├── json_parser.py
│   │           │   ├── log_capture.py
│   │           │   ├── matchers.py
│   │           │   ├── model.py
│   │           │   ├── model_core.py
│   │           │   ├── model_describe.py
│   │           │   ├── parser.py
│   │           │   ├── reporter
│   │           │   │   ├── __init__.py
│   │           │   │   ├── base.py
│   │           │   │   ├── junit.py
│   │           │   │   └── summary.py
│   │           │   ├── runner.py
│   │           │   ├── runner_util.py
│   │           │   ├── step_registry.py
│   │           │   ├── tag_expression.py
│   │           │   ├── tag_matcher.py
│   │           │   ├── textutil.py
│   │           │   └── userdata.py
│   │           ├── behave-1.2.6.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   ├── metadata.json
│   │           │   ├── top_level.txt
│   │           │   └── zip-safe
│   │           ├── black
│   │           │   ├── __init__.cpython-312-darwin.so
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _width_table.cpython-312-darwin.so
│   │           │   ├── _width_table.py
│   │           │   ├── brackets.cpython-312-darwin.so
│   │           │   ├── brackets.py
│   │           │   ├── cache.cpython-312-darwin.so
│   │           │   ├── cache.py
│   │           │   ├── comments.cpython-312-darwin.so
│   │           │   ├── comments.py
│   │           │   ├── concurrency.py
│   │           │   ├── const.cpython-312-darwin.so
│   │           │   ├── const.py
│   │           │   ├── debug.py
│   │           │   ├── files.py
│   │           │   ├── handle_ipynb_magics.cpython-312-darwin.so
│   │           │   ├── handle_ipynb_magics.py
│   │           │   ├── linegen.cpython-312-darwin.so
│   │           │   ├── linegen.py
│   │           │   ├── lines.cpython-312-darwin.so
│   │           │   ├── lines.py
│   │           │   ├── mode.cpython-312-darwin.so
│   │           │   ├── mode.py
│   │           │   ├── nodes.cpython-312-darwin.so
│   │           │   ├── nodes.py
│   │           │   ├── numerics.cpython-312-darwin.so
│   │           │   ├── numerics.py
│   │           │   ├── output.py
│   │           │   ├── parsing.cpython-312-darwin.so
│   │           │   ├── parsing.py
│   │           │   ├── py.typed
│   │           │   ├── ranges.cpython-312-darwin.so
│   │           │   ├── ranges.py
│   │           │   ├── report.py
│   │           │   ├── resources
│   │           │   │   ├── __init__.cpython-312-darwin.so
│   │           │   │   ├── __init__.py
│   │           │   │   └── black.schema.json
│   │           │   ├── rusty.cpython-312-darwin.so
│   │           │   ├── rusty.py
│   │           │   ├── schema.cpython-312-darwin.so
│   │           │   ├── schema.py
│   │           │   ├── strings.cpython-312-darwin.so
│   │           │   ├── strings.py
│   │           │   ├── trans.cpython-312-darwin.so
│   │           │   └── trans.py
│   │           ├── black-25.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       ├── AUTHORS.md
│   │           │       └── LICENSE
│   │           ├── blackd
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── middlewares.py
│   │           ├── blib2to3
│   │           │   ├── Grammar.txt
│   │           │   ├── LICENSE
│   │           │   ├── PatternGrammar.txt
│   │           │   ├── README
│   │           │   ├── __init__.py
│   │           │   ├── pgen2
│   │           │   │   ├── __init__.py
│   │           │   │   ├── conv.cpython-312-darwin.so
│   │           │   │   ├── conv.py
│   │           │   │   ├── driver.cpython-312-darwin.so
│   │           │   │   ├── driver.py
│   │           │   │   ├── grammar.cpython-312-darwin.so
│   │           │   │   ├── grammar.py
│   │           │   │   ├── literals.cpython-312-darwin.so
│   │           │   │   ├── literals.py
│   │           │   │   ├── parse.cpython-312-darwin.so
│   │           │   │   ├── parse.py
│   │           │   │   ├── pgen.cpython-312-darwin.so
│   │           │   │   ├── pgen.py
│   │           │   │   ├── token.cpython-312-darwin.so
│   │           │   │   ├── token.py
│   │           │   │   ├── tokenize.cpython-312-darwin.so
│   │           │   │   └── tokenize.py
│   │           │   ├── pygram.cpython-312-darwin.so
│   │           │   ├── pygram.py
│   │           │   ├── pytree.cpython-312-darwin.so
│   │           │   └── pytree.py
│   │           ├── certifi
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── cacert.pem
│   │           │   ├── core.py
│   │           │   └── py.typed
│   │           ├── certifi-2025.1.31.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── cfgv-3.4.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── cfgv.py
│   │           ├── charset_normalizer
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── api.py
│   │           │   ├── cd.py
│   │           │   ├── cli
│   │           │   │   ├── __init__.py
│   │           │   │   └── __main__.py
│   │           │   ├── constant.py
│   │           │   ├── legacy.py
│   │           │   ├── md.cpython-312-darwin.so
│   │           │   ├── md.py
│   │           │   ├── md__mypyc.cpython-312-darwin.so
│   │           │   ├── models.py
│   │           │   ├── py.typed
│   │           │   ├── utils.py
│   │           │   └── version.py
│   │           ├── charset_normalizer-3.4.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── click
│   │           │   ├── __init__.py
│   │           │   ├── _compat.py
│   │           │   ├── _termui_impl.py
│   │           │   ├── _textwrap.py
│   │           │   ├── _winconsole.py
│   │           │   ├── core.py
│   │           │   ├── decorators.py
│   │           │   ├── exceptions.py
│   │           │   ├── formatting.py
│   │           │   ├── globals.py
│   │           │   ├── parser.py
│   │           │   ├── py.typed
│   │           │   ├── shell_completion.py
│   │           │   ├── termui.py
│   │           │   ├── testing.py
│   │           │   ├── types.py
│   │           │   └── utils.py
│   │           ├── click-8.1.8.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── distlib
│   │           │   ├── __init__.py
│   │           │   ├── compat.py
│   │           │   ├── database.py
│   │           │   ├── index.py
│   │           │   ├── locators.py
│   │           │   ├── manifest.py
│   │           │   ├── markers.py
│   │           │   ├── metadata.py
│   │           │   ├── resources.py
│   │           │   ├── scripts.py
│   │           │   ├── t32.exe
│   │           │   ├── t64-arm.exe
│   │           │   ├── t64.exe
│   │           │   ├── util.py
│   │           │   ├── version.py
│   │           │   ├── w32.exe
│   │           │   ├── w64-arm.exe
│   │           │   ├── w64.exe
│   │           │   └── wheel.py
│   │           ├── distlib-0.3.9.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── distro
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── distro.py
│   │           │   └── py.typed
│   │           ├── distro-1.9.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── fastapi
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _compat.py
│   │           │   ├── applications.py
│   │           │   ├── background.py
│   │           │   ├── cli.py
│   │           │   ├── concurrency.py
│   │           │   ├── datastructures.py
│   │           │   ├── dependencies
│   │           │   │   ├── __init__.py
│   │           │   │   ├── models.py
│   │           │   │   └── utils.py
│   │           │   ├── encoders.py
│   │           │   ├── exception_handlers.py
│   │           │   ├── exceptions.py
│   │           │   ├── logger.py
│   │           │   ├── middleware
│   │           │   │   ├── __init__.py
│   │           │   │   ├── cors.py
│   │           │   │   ├── gzip.py
│   │           │   │   ├── httpsredirect.py
│   │           │   │   ├── trustedhost.py
│   │           │   │   └── wsgi.py
│   │           │   ├── openapi
│   │           │   │   ├── __init__.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── docs.py
│   │           │   │   ├── models.py
│   │           │   │   └── utils.py
│   │           │   ├── param_functions.py
│   │           │   ├── params.py
│   │           │   ├── py.typed
│   │           │   ├── requests.py
│   │           │   ├── responses.py
│   │           │   ├── routing.py
│   │           │   ├── security
│   │           │   │   ├── __init__.py
│   │           │   │   ├── api_key.py
│   │           │   │   ├── base.py
│   │           │   │   ├── http.py
│   │           │   │   ├── oauth2.py
│   │           │   │   ├── open_id_connect_url.py
│   │           │   │   └── utils.py
│   │           │   ├── staticfiles.py
│   │           │   ├── templating.py
│   │           │   ├── testclient.py
│   │           │   ├── types.py
│   │           │   ├── utils.py
│   │           │   └── websockets.py
│   │           ├── fastapi-0.115.12.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── filelock
│   │           │   ├── __init__.py
│   │           │   ├── _api.py
│   │           │   ├── _error.py
│   │           │   ├── _soft.py
│   │           │   ├── _unix.py
│   │           │   ├── _util.py
│   │           │   ├── _windows.py
│   │           │   ├── asyncio.py
│   │           │   ├── py.typed
│   │           │   └── version.py
│   │           ├── filelock-3.18.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── h11
│   │           │   ├── __init__.py
│   │           │   ├── _abnf.py
│   │           │   ├── _connection.py
│   │           │   ├── _events.py
│   │           │   ├── _headers.py
│   │           │   ├── _readers.py
│   │           │   ├── _receivebuffer.py
│   │           │   ├── _state.py
│   │           │   ├── _util.py
│   │           │   ├── _version.py
│   │           │   ├── _writers.py
│   │           │   ├── py.typed
│   │           │   └── tests
│   │           │       ├── __init__.py
│   │           │       ├── data
│   │           │       │   └── test-file
│   │           │       ├── helpers.py
│   │           │       ├── test_against_stdlib_http.py
│   │           │       ├── test_connection.py
│   │           │       ├── test_events.py
│   │           │       ├── test_headers.py
│   │           │       ├── test_helpers.py
│   │           │       ├── test_io.py
│   │           │       ├── test_receivebuffer.py
│   │           │       ├── test_state.py
│   │           │       └── test_util.py
│   │           ├── h11-0.14.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── httpcore
│   │           │   ├── __init__.py
│   │           │   ├── _api.py
│   │           │   ├── _async
│   │           │   │   ├── __init__.py
│   │           │   │   ├── connection.py
│   │           │   │   ├── connection_pool.py
│   │           │   │   ├── http11.py
│   │           │   │   ├── http2.py
│   │           │   │   ├── http_proxy.py
│   │           │   │   ├── interfaces.py
│   │           │   │   └── socks_proxy.py
│   │           │   ├── _backends
│   │           │   │   ├── __init__.py
│   │           │   │   ├── anyio.py
│   │           │   │   ├── auto.py
│   │           │   │   ├── base.py
│   │           │   │   ├── mock.py
│   │           │   │   ├── sync.py
│   │           │   │   └── trio.py
│   │           │   ├── _exceptions.py
│   │           │   ├── _models.py
│   │           │   ├── _ssl.py
│   │           │   ├── _sync
│   │           │   │   ├── __init__.py
│   │           │   │   ├── connection.py
│   │           │   │   ├── connection_pool.py
│   │           │   │   ├── http11.py
│   │           │   │   ├── http2.py
│   │           │   │   ├── http_proxy.py
│   │           │   │   ├── interfaces.py
│   │           │   │   └── socks_proxy.py
│   │           │   ├── _synchronization.py
│   │           │   ├── _trace.py
│   │           │   ├── _utils.py
│   │           │   └── py.typed
│   │           ├── httpcore-1.0.7.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE.md
│   │           ├── httpx
│   │           │   ├── __init__.py
│   │           │   ├── __version__.py
│   │           │   ├── _api.py
│   │           │   ├── _auth.py
│   │           │   ├── _client.py
│   │           │   ├── _config.py
│   │           │   ├── _content.py
│   │           │   ├── _decoders.py
│   │           │   ├── _exceptions.py
│   │           │   ├── _main.py
│   │           │   ├── _models.py
│   │           │   ├── _multipart.py
│   │           │   ├── _status_codes.py
│   │           │   ├── _transports
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asgi.py
│   │           │   │   ├── base.py
│   │           │   │   ├── default.py
│   │           │   │   ├── mock.py
│   │           │   │   └── wsgi.py
│   │           │   ├── _types.py
│   │           │   ├── _urlparse.py
│   │           │   ├── _urls.py
│   │           │   ├── _utils.py
│   │           │   └── py.typed
│   │           ├── httpx-0.28.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE.md
│   │           ├── identify
│   │           │   ├── __init__.py
│   │           │   ├── cli.py
│   │           │   ├── extensions.py
│   │           │   ├── identify.py
│   │           │   ├── interpreters.py
│   │           │   ├── py.typed
│   │           │   └── vendor
│   │           │       ├── __init__.py
│   │           │       └── licenses.py
│   │           ├── identify-2.6.9.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── idna
│   │           │   ├── __init__.py
│   │           │   ├── codec.py
│   │           │   ├── compat.py
│   │           │   ├── core.py
│   │           │   ├── idnadata.py
│   │           │   ├── intranges.py
│   │           │   ├── package_data.py
│   │           │   ├── py.typed
│   │           │   └── uts46data.py
│   │           ├── idna-3.10.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.md
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── iniconfig
│   │           │   ├── __init__.py
│   │           │   ├── _parse.py
│   │           │   ├── _version.py
│   │           │   ├── exceptions.py
│   │           │   └── py.typed
│   │           ├── iniconfig-2.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── isort
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _vendored
│   │           │   │   └── tomli
│   │           │   │       ├── LICENSE
│   │           │   │       ├── __init__.py
│   │           │   │       ├── _parser.py
│   │           │   │       ├── _re.py
│   │           │   │       └── py.typed
│   │           │   ├── _version.py
│   │           │   ├── api.py
│   │           │   ├── comments.py
│   │           │   ├── core.py
│   │           │   ├── deprecated
│   │           │   │   ├── __init__.py
│   │           │   │   └── finders.py
│   │           │   ├── exceptions.py
│   │           │   ├── files.py
│   │           │   ├── format.py
│   │           │   ├── hooks.py
│   │           │   ├── identify.py
│   │           │   ├── io.py
│   │           │   ├── literal.py
│   │           │   ├── logo.py
│   │           │   ├── main.py
│   │           │   ├── output.py
│   │           │   ├── parse.py
│   │           │   ├── place.py
│   │           │   ├── profiles.py
│   │           │   ├── py.typed
│   │           │   ├── pylama_isort.py
│   │           │   ├── sections.py
│   │           │   ├── settings.py
│   │           │   ├── setuptools_commands.py
│   │           │   ├── sorting.py
│   │           │   ├── stdlibs
│   │           │   │   ├── __init__.py
│   │           │   │   ├── all.py
│   │           │   │   ├── py2.py
│   │           │   │   ├── py27.py
│   │           │   │   ├── py3.py
│   │           │   │   ├── py310.py
│   │           │   │   ├── py311.py
│   │           │   │   ├── py312.py
│   │           │   │   ├── py313.py
│   │           │   │   ├── py36.py
│   │           │   │   ├── py37.py
│   │           │   │   ├── py38.py
│   │           │   │   └── py39.py
│   │           │   ├── utils.py
│   │           │   ├── wrap.py
│   │           │   └── wrap_modes.py
│   │           ├── isort-6.0.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── jiter
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── jiter.cpython-312-darwin.so
│   │           │   └── py.typed
│   │           ├── jiter-0.9.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── mypy_extensions-1.0.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── mypy_extensions.py
│   │           ├── nodeenv-1.9.1.dist-info
│   │           │   ├── AUTHORS
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── nodeenv.py
│   │           ├── openai
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _base_client.py
│   │           │   ├── _client.py
│   │           │   ├── _compat.py
│   │           │   ├── _constants.py
│   │           │   ├── _exceptions.py
│   │           │   ├── _extras
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _common.py
│   │           │   │   ├── numpy_proxy.py
│   │           │   │   ├── pandas_proxy.py
│   │           │   │   └── sounddevice_proxy.py
│   │           │   ├── _files.py
│   │           │   ├── _legacy_response.py
│   │           │   ├── _models.py
│   │           │   ├── _module_client.py
│   │           │   ├── _qs.py
│   │           │   ├── _resource.py
│   │           │   ├── _response.py
│   │           │   ├── _streaming.py
│   │           │   ├── _types.py
│   │           │   ├── _utils
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _logs.py
│   │           │   │   ├── _proxy.py
│   │           │   │   ├── _reflection.py
│   │           │   │   ├── _streams.py
│   │           │   │   ├── _sync.py
│   │           │   │   ├── _transform.py
│   │           │   │   ├── _typing.py
│   │           │   │   └── _utils.py
│   │           │   ├── _version.py
│   │           │   ├── cli
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _api
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _main.py
│   │           │   │   │   ├── audio.py
│   │           │   │   │   ├── chat
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── completions.py
│   │           │   │   │   ├── completions.py
│   │           │   │   │   ├── files.py
│   │           │   │   │   ├── image.py
│   │           │   │   │   └── models.py
│   │           │   │   ├── _cli.py
│   │           │   │   ├── _errors.py
│   │           │   │   ├── _models.py
│   │           │   │   ├── _progress.py
│   │           │   │   ├── _tools
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _main.py
│   │           │   │   │   ├── fine_tunes.py
│   │           │   │   │   └── migrate.py
│   │           │   │   └── _utils.py
│   │           │   ├── helpers
│   │           │   │   ├── __init__.py
│   │           │   │   ├── local_audio_player.py
│   │           │   │   └── microphone.py
│   │           │   ├── lib
│   │           │   │   ├── .keep
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _old_api.py
│   │           │   │   ├── _parsing
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _completions.py
│   │           │   │   │   └── _responses.py
│   │           │   │   ├── _pydantic.py
│   │           │   │   ├── _tools.py
│   │           │   │   ├── _validators.py
│   │           │   │   ├── azure.py
│   │           │   │   └── streaming
│   │           │   │       ├── __init__.py
│   │           │   │       ├── _assistants.py
│   │           │   │       ├── _deltas.py
│   │           │   │       ├── chat
│   │           │   │       │   ├── __init__.py
│   │           │   │       │   ├── _completions.py
│   │           │   │       │   ├── _events.py
│   │           │   │       │   └── _types.py
│   │           │   │       └── responses
│   │           │   │           ├── __init__.py
│   │           │   │           ├── _events.py
│   │           │   │           ├── _responses.py
│   │           │   │           └── _types.py
│   │           │   ├── pagination.py
│   │           │   ├── py.typed
│   │           │   ├── resources
│   │           │   │   ├── __init__.py
│   │           │   │   ├── audio
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── audio.py
│   │           │   │   │   ├── speech.py
│   │           │   │   │   ├── transcriptions.py
│   │           │   │   │   └── translations.py
│   │           │   │   ├── batches.py
│   │           │   │   ├── beta
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── assistants.py
│   │           │   │   │   ├── beta.py
│   │           │   │   │   ├── chat
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── chat.py
│   │           │   │   │   │   └── completions.py
│   │           │   │   │   ├── realtime
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── realtime.py
│   │           │   │   │   │   ├── sessions.py
│   │           │   │   │   │   └── transcription_sessions.py
│   │           │   │   │   └── threads
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── messages.py
│   │           │   │   │       ├── runs
│   │           │   │   │       │   ├── __init__.py
│   │           │   │   │       │   ├── runs.py
│   │           │   │   │       │   └── steps.py
│   │           │   │   │       └── threads.py
│   │           │   │   ├── chat
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── chat.py
│   │           │   │   │   └── completions
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── completions.py
│   │           │   │   │       └── messages.py
│   │           │   │   ├── completions.py
│   │           │   │   ├── embeddings.py
│   │           │   │   ├── files.py
│   │           │   │   ├── fine_tuning
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── fine_tuning.py
│   │           │   │   │   └── jobs
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── checkpoints.py
│   │           │   │   │       └── jobs.py
│   │           │   │   ├── images.py
│   │           │   │   ├── models.py
│   │           │   │   ├── moderations.py
│   │           │   │   ├── responses
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── input_items.py
│   │           │   │   │   └── responses.py
│   │           │   │   ├── uploads
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── parts.py
│   │           │   │   │   └── uploads.py
│   │           │   │   └── vector_stores
│   │           │   │       ├── __init__.py
│   │           │   │       ├── file_batches.py
│   │           │   │       ├── files.py
│   │           │   │       └── vector_stores.py
│   │           │   ├── types
│   │           │   │   ├── __init__.py
│   │           │   │   ├── audio
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── speech_create_params.py
│   │           │   │   │   ├── speech_model.py
│   │           │   │   │   ├── transcription.py
│   │           │   │   │   ├── transcription_create_params.py
│   │           │   │   │   ├── transcription_create_response.py
│   │           │   │   │   ├── transcription_include.py
│   │           │   │   │   ├── transcription_segment.py
│   │           │   │   │   ├── transcription_stream_event.py
│   │           │   │   │   ├── transcription_text_delta_event.py
│   │           │   │   │   ├── transcription_text_done_event.py
│   │           │   │   │   ├── transcription_verbose.py
│   │           │   │   │   ├── transcription_word.py
│   │           │   │   │   ├── translation.py
│   │           │   │   │   ├── translation_create_params.py
│   │           │   │   │   ├── translation_create_response.py
│   │           │   │   │   └── translation_verbose.py
│   │           │   │   ├── audio_model.py
│   │           │   │   ├── audio_response_format.py
│   │           │   │   ├── auto_file_chunking_strategy_param.py
│   │           │   │   ├── batch.py
│   │           │   │   ├── batch_create_params.py
│   │           │   │   ├── batch_error.py
│   │           │   │   ├── batch_list_params.py
│   │           │   │   ├── batch_request_counts.py
│   │           │   │   ├── beta
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── assistant.py
│   │           │   │   │   ├── assistant_create_params.py
│   │           │   │   │   ├── assistant_deleted.py
│   │           │   │   │   ├── assistant_list_params.py
│   │           │   │   │   ├── assistant_response_format_option.py
│   │           │   │   │   ├── assistant_response_format_option_param.py
│   │           │   │   │   ├── assistant_stream_event.py
│   │           │   │   │   ├── assistant_tool.py
│   │           │   │   │   ├── assistant_tool_choice.py
│   │           │   │   │   ├── assistant_tool_choice_function.py
│   │           │   │   │   ├── assistant_tool_choice_function_param.py
│   │           │   │   │   ├── assistant_tool_choice_option.py
│   │           │   │   │   ├── assistant_tool_choice_option_param.py
│   │           │   │   │   ├── assistant_tool_choice_param.py
│   │           │   │   │   ├── assistant_tool_param.py
│   │           │   │   │   ├── assistant_update_params.py
│   │           │   │   │   ├── chat
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── code_interpreter_tool.py
│   │           │   │   │   ├── code_interpreter_tool_param.py
│   │           │   │   │   ├── file_search_tool.py
│   │           │   │   │   ├── file_search_tool_param.py
│   │           │   │   │   ├── function_tool.py
│   │           │   │   │   ├── function_tool_param.py
│   │           │   │   │   ├── realtime
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── conversation_created_event.py
│   │           │   │   │   │   ├── conversation_item.py
│   │           │   │   │   │   ├── conversation_item_content.py
│   │           │   │   │   │   ├── conversation_item_content_param.py
│   │           │   │   │   │   ├── conversation_item_create_event.py
│   │           │   │   │   │   ├── conversation_item_create_event_param.py
│   │           │   │   │   │   ├── conversation_item_created_event.py
│   │           │   │   │   │   ├── conversation_item_delete_event.py
│   │           │   │   │   │   ├── conversation_item_delete_event_param.py
│   │           │   │   │   │   ├── conversation_item_deleted_event.py
│   │           │   │   │   │   ├── conversation_item_input_audio_transcription_completed_event.py
│   │           │   │   │   │   ├── conversation_item_input_audio_transcription_delta_event.py
│   │           │   │   │   │   ├── conversation_item_input_audio_transcription_failed_event.py
│   │           │   │   │   │   ├── conversation_item_param.py
│   │           │   │   │   │   ├── conversation_item_retrieve_event.py
│   │           │   │   │   │   ├── conversation_item_retrieve_event_param.py
│   │           │   │   │   │   ├── conversation_item_truncate_event.py
│   │           │   │   │   │   ├── conversation_item_truncate_event_param.py
│   │           │   │   │   │   ├── conversation_item_truncated_event.py
│   │           │   │   │   │   ├── conversation_item_with_reference.py
│   │           │   │   │   │   ├── conversation_item_with_reference_param.py
│   │           │   │   │   │   ├── error_event.py
│   │           │   │   │   │   ├── input_audio_buffer_append_event.py
│   │           │   │   │   │   ├── input_audio_buffer_append_event_param.py
│   │           │   │   │   │   ├── input_audio_buffer_clear_event.py
│   │           │   │   │   │   ├── input_audio_buffer_clear_event_param.py
│   │           │   │   │   │   ├── input_audio_buffer_cleared_event.py
│   │           │   │   │   │   ├── input_audio_buffer_commit_event.py
│   │           │   │   │   │   ├── input_audio_buffer_commit_event_param.py
│   │           │   │   │   │   ├── input_audio_buffer_committed_event.py
│   │           │   │   │   │   ├── input_audio_buffer_speech_started_event.py
│   │           │   │   │   │   ├── input_audio_buffer_speech_stopped_event.py
│   │           │   │   │   │   ├── rate_limits_updated_event.py
│   │           │   │   │   │   ├── realtime_client_event.py
│   │           │   │   │   │   ├── realtime_client_event_param.py
│   │           │   │   │   │   ├── realtime_connect_params.py
│   │           │   │   │   │   ├── realtime_response.py
│   │           │   │   │   │   ├── realtime_response_status.py
│   │           │   │   │   │   ├── realtime_response_usage.py
│   │           │   │   │   │   ├── realtime_server_event.py
│   │           │   │   │   │   ├── response_audio_delta_event.py
│   │           │   │   │   │   ├── response_audio_done_event.py
│   │           │   │   │   │   ├── response_audio_transcript_delta_event.py
│   │           │   │   │   │   ├── response_audio_transcript_done_event.py
│   │           │   │   │   │   ├── response_cancel_event.py
│   │           │   │   │   │   ├── response_cancel_event_param.py
│   │           │   │   │   │   ├── response_content_part_added_event.py
│   │           │   │   │   │   ├── response_content_part_done_event.py
│   │           │   │   │   │   ├── response_create_event.py
│   │           │   │   │   │   ├── response_create_event_param.py
│   │           │   │   │   │   ├── response_created_event.py
│   │           │   │   │   │   ├── response_done_event.py
│   │           │   │   │   │   ├── response_function_call_arguments_delta_event.py
│   │           │   │   │   │   ├── response_function_call_arguments_done_event.py
│   │           │   │   │   │   ├── response_output_item_added_event.py
│   │           │   │   │   │   ├── response_output_item_done_event.py
│   │           │   │   │   │   ├── response_text_delta_event.py
│   │           │   │   │   │   ├── response_text_done_event.py
│   │           │   │   │   │   ├── session.py
│   │           │   │   │   │   ├── session_create_params.py
│   │           │   │   │   │   ├── session_create_response.py
│   │           │   │   │   │   ├── session_created_event.py
│   │           │   │   │   │   ├── session_update_event.py
│   │           │   │   │   │   ├── session_update_event_param.py
│   │           │   │   │   │   ├── session_updated_event.py
│   │           │   │   │   │   ├── transcription_session.py
│   │           │   │   │   │   ├── transcription_session_create_params.py
│   │           │   │   │   │   ├── transcription_session_update.py
│   │           │   │   │   │   ├── transcription_session_update_param.py
│   │           │   │   │   │   └── transcription_session_updated_event.py
│   │           │   │   │   ├── thread.py
│   │           │   │   │   ├── thread_create_and_run_params.py
│   │           │   │   │   ├── thread_create_params.py
│   │           │   │   │   ├── thread_deleted.py
│   │           │   │   │   ├── thread_update_params.py
│   │           │   │   │   └── threads
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── annotation.py
│   │           │   │   │       ├── annotation_delta.py
│   │           │   │   │       ├── file_citation_annotation.py
│   │           │   │   │       ├── file_citation_delta_annotation.py
│   │           │   │   │       ├── file_path_annotation.py
│   │           │   │   │       ├── file_path_delta_annotation.py
│   │           │   │   │       ├── image_file.py
│   │           │   │   │       ├── image_file_content_block.py
│   │           │   │   │       ├── image_file_content_block_param.py
│   │           │   │   │       ├── image_file_delta.py
│   │           │   │   │       ├── image_file_delta_block.py
│   │           │   │   │       ├── image_file_param.py
│   │           │   │   │       ├── image_url.py
│   │           │   │   │       ├── image_url_content_block.py
│   │           │   │   │       ├── image_url_content_block_param.py
│   │           │   │   │       ├── image_url_delta.py
│   │           │   │   │       ├── image_url_delta_block.py
│   │           │   │   │       ├── image_url_param.py
│   │           │   │   │       ├── message.py
│   │           │   │   │       ├── message_content.py
│   │           │   │   │       ├── message_content_delta.py
│   │           │   │   │       ├── message_content_part_param.py
│   │           │   │   │       ├── message_create_params.py
│   │           │   │   │       ├── message_deleted.py
│   │           │   │   │       ├── message_delta.py
│   │           │   │   │       ├── message_delta_event.py
│   │           │   │   │       ├── message_list_params.py
│   │           │   │   │       ├── message_update_params.py
│   │           │   │   │       ├── refusal_content_block.py
│   │           │   │   │       ├── refusal_delta_block.py
│   │           │   │   │       ├── required_action_function_tool_call.py
│   │           │   │   │       ├── run.py
│   │           │   │   │       ├── run_create_params.py
│   │           │   │   │       ├── run_list_params.py
│   │           │   │   │       ├── run_status.py
│   │           │   │   │       ├── run_submit_tool_outputs_params.py
│   │           │   │   │       ├── run_update_params.py
│   │           │   │   │       ├── runs
│   │           │   │   │       │   ├── __init__.py
│   │           │   │   │       │   ├── code_interpreter_logs.py
│   │           │   │   │       │   ├── code_interpreter_output_image.py
│   │           │   │   │       │   ├── code_interpreter_tool_call.py
│   │           │   │   │       │   ├── code_interpreter_tool_call_delta.py
│   │           │   │   │       │   ├── file_search_tool_call.py
│   │           │   │   │       │   ├── file_search_tool_call_delta.py
│   │           │   │   │       │   ├── function_tool_call.py
│   │           │   │   │       │   ├── function_tool_call_delta.py
│   │           │   │   │       │   ├── message_creation_step_details.py
│   │           │   │   │       │   ├── run_step.py
│   │           │   │   │       │   ├── run_step_delta.py
│   │           │   │   │       │   ├── run_step_delta_event.py
│   │           │   │   │       │   ├── run_step_delta_message_delta.py
│   │           │   │   │       │   ├── run_step_include.py
│   │           │   │   │       │   ├── step_list_params.py
│   │           │   │   │       │   ├── step_retrieve_params.py
│   │           │   │   │       │   ├── tool_call.py
│   │           │   │   │       │   ├── tool_call_delta.py
│   │           │   │   │       │   ├── tool_call_delta_object.py
│   │           │   │   │       │   └── tool_calls_step_details.py
│   │           │   │   │       ├── text.py
│   │           │   │   │       ├── text_content_block.py
│   │           │   │   │       ├── text_content_block_param.py
│   │           │   │   │       ├── text_delta.py
│   │           │   │   │       └── text_delta_block.py
│   │           │   │   ├── chat
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── chat_completion.py
│   │           │   │   │   ├── chat_completion_assistant_message_param.py
│   │           │   │   │   ├── chat_completion_audio.py
│   │           │   │   │   ├── chat_completion_audio_param.py
│   │           │   │   │   ├── chat_completion_chunk.py
│   │           │   │   │   ├── chat_completion_content_part_image_param.py
│   │           │   │   │   ├── chat_completion_content_part_input_audio_param.py
│   │           │   │   │   ├── chat_completion_content_part_param.py
│   │           │   │   │   ├── chat_completion_content_part_refusal_param.py
│   │           │   │   │   ├── chat_completion_content_part_text_param.py
│   │           │   │   │   ├── chat_completion_deleted.py
│   │           │   │   │   ├── chat_completion_developer_message_param.py
│   │           │   │   │   ├── chat_completion_function_call_option_param.py
│   │           │   │   │   ├── chat_completion_function_message_param.py
│   │           │   │   │   ├── chat_completion_message.py
│   │           │   │   │   ├── chat_completion_message_param.py
│   │           │   │   │   ├── chat_completion_message_tool_call.py
│   │           │   │   │   ├── chat_completion_message_tool_call_param.py
│   │           │   │   │   ├── chat_completion_modality.py
│   │           │   │   │   ├── chat_completion_named_tool_choice_param.py
│   │           │   │   │   ├── chat_completion_prediction_content_param.py
│   │           │   │   │   ├── chat_completion_reasoning_effort.py
│   │           │   │   │   ├── chat_completion_role.py
│   │           │   │   │   ├── chat_completion_store_message.py
│   │           │   │   │   ├── chat_completion_stream_options_param.py
│   │           │   │   │   ├── chat_completion_system_message_param.py
│   │           │   │   │   ├── chat_completion_token_logprob.py
│   │           │   │   │   ├── chat_completion_tool_choice_option_param.py
│   │           │   │   │   ├── chat_completion_tool_message_param.py
│   │           │   │   │   ├── chat_completion_tool_param.py
│   │           │   │   │   ├── chat_completion_user_message_param.py
│   │           │   │   │   ├── completion_create_params.py
│   │           │   │   │   ├── completion_list_params.py
│   │           │   │   │   ├── completion_update_params.py
│   │           │   │   │   ├── completions
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── message_list_params.py
│   │           │   │   │   ├── parsed_chat_completion.py
│   │           │   │   │   └── parsed_function_tool_call.py
│   │           │   │   ├── chat_model.py
│   │           │   │   ├── completion.py
│   │           │   │   ├── completion_choice.py
│   │           │   │   ├── completion_create_params.py
│   │           │   │   ├── completion_usage.py
│   │           │   │   ├── create_embedding_response.py
│   │           │   │   ├── embedding.py
│   │           │   │   ├── embedding_create_params.py
│   │           │   │   ├── embedding_model.py
│   │           │   │   ├── file_chunking_strategy.py
│   │           │   │   ├── file_chunking_strategy_param.py
│   │           │   │   ├── file_content.py
│   │           │   │   ├── file_create_params.py
│   │           │   │   ├── file_deleted.py
│   │           │   │   ├── file_list_params.py
│   │           │   │   ├── file_object.py
│   │           │   │   ├── file_purpose.py
│   │           │   │   ├── fine_tuning
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── fine_tuning_job.py
│   │           │   │   │   ├── fine_tuning_job_event.py
│   │           │   │   │   ├── fine_tuning_job_integration.py
│   │           │   │   │   ├── fine_tuning_job_wandb_integration.py
│   │           │   │   │   ├── fine_tuning_job_wandb_integration_object.py
│   │           │   │   │   ├── job_create_params.py
│   │           │   │   │   ├── job_list_events_params.py
│   │           │   │   │   ├── job_list_params.py
│   │           │   │   │   └── jobs
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── checkpoint_list_params.py
│   │           │   │   │       └── fine_tuning_job_checkpoint.py
│   │           │   │   ├── image.py
│   │           │   │   ├── image_create_variation_params.py
│   │           │   │   ├── image_edit_params.py
│   │           │   │   ├── image_generate_params.py
│   │           │   │   ├── image_model.py
│   │           │   │   ├── images_response.py
│   │           │   │   ├── model.py
│   │           │   │   ├── model_deleted.py
│   │           │   │   ├── moderation.py
│   │           │   │   ├── moderation_create_params.py
│   │           │   │   ├── moderation_create_response.py
│   │           │   │   ├── moderation_image_url_input_param.py
│   │           │   │   ├── moderation_model.py
│   │           │   │   ├── moderation_multi_modal_input_param.py
│   │           │   │   ├── moderation_text_input_param.py
│   │           │   │   ├── other_file_chunking_strategy_object.py
│   │           │   │   ├── responses
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── computer_tool.py
│   │           │   │   │   ├── computer_tool_param.py
│   │           │   │   │   ├── easy_input_message_param.py
│   │           │   │   │   ├── file_search_tool.py
│   │           │   │   │   ├── file_search_tool_param.py
│   │           │   │   │   ├── function_tool.py
│   │           │   │   │   ├── function_tool_param.py
│   │           │   │   │   ├── input_item_list_params.py
│   │           │   │   │   ├── parsed_response.py
│   │           │   │   │   ├── response.py
│   │           │   │   │   ├── response_audio_delta_event.py
│   │           │   │   │   ├── response_audio_done_event.py
│   │           │   │   │   ├── response_audio_transcript_delta_event.py
│   │           │   │   │   ├── response_audio_transcript_done_event.py
│   │           │   │   │   ├── response_code_interpreter_call_code_delta_event.py
│   │           │   │   │   ├── response_code_interpreter_call_code_done_event.py
│   │           │   │   │   ├── response_code_interpreter_call_completed_event.py
│   │           │   │   │   ├── response_code_interpreter_call_in_progress_event.py
│   │           │   │   │   ├── response_code_interpreter_call_interpreting_event.py
│   │           │   │   │   ├── response_code_interpreter_tool_call.py
│   │           │   │   │   ├── response_completed_event.py
│   │           │   │   │   ├── response_computer_tool_call.py
│   │           │   │   │   ├── response_computer_tool_call_output_item.py
│   │           │   │   │   ├── response_computer_tool_call_output_screenshot.py
│   │           │   │   │   ├── response_computer_tool_call_output_screenshot_param.py
│   │           │   │   │   ├── response_computer_tool_call_param.py
│   │           │   │   │   ├── response_content_part_added_event.py
│   │           │   │   │   ├── response_content_part_done_event.py
│   │           │   │   │   ├── response_create_params.py
│   │           │   │   │   ├── response_created_event.py
│   │           │   │   │   ├── response_error.py
│   │           │   │   │   ├── response_error_event.py
│   │           │   │   │   ├── response_failed_event.py
│   │           │   │   │   ├── response_file_search_call_completed_event.py
│   │           │   │   │   ├── response_file_search_call_in_progress_event.py
│   │           │   │   │   ├── response_file_search_call_searching_event.py
│   │           │   │   │   ├── response_file_search_tool_call.py
│   │           │   │   │   ├── response_file_search_tool_call_param.py
│   │           │   │   │   ├── response_format_text_config.py
│   │           │   │   │   ├── response_format_text_config_param.py
│   │           │   │   │   ├── response_format_text_json_schema_config.py
│   │           │   │   │   ├── response_format_text_json_schema_config_param.py
│   │           │   │   │   ├── response_function_call_arguments_delta_event.py
│   │           │   │   │   ├── response_function_call_arguments_done_event.py
│   │           │   │   │   ├── response_function_tool_call.py
│   │           │   │   │   ├── response_function_tool_call_item.py
│   │           │   │   │   ├── response_function_tool_call_output_item.py
│   │           │   │   │   ├── response_function_tool_call_param.py
│   │           │   │   │   ├── response_function_web_search.py
│   │           │   │   │   ├── response_function_web_search_param.py
│   │           │   │   │   ├── response_in_progress_event.py
│   │           │   │   │   ├── response_includable.py
│   │           │   │   │   ├── response_incomplete_event.py
│   │           │   │   │   ├── response_input_content.py
│   │           │   │   │   ├── response_input_content_param.py
│   │           │   │   │   ├── response_input_file.py
│   │           │   │   │   ├── response_input_file_param.py
│   │           │   │   │   ├── response_input_image.py
│   │           │   │   │   ├── response_input_image_param.py
│   │           │   │   │   ├── response_input_item_param.py
│   │           │   │   │   ├── response_input_message_content_list.py
│   │           │   │   │   ├── response_input_message_content_list_param.py
│   │           │   │   │   ├── response_input_message_item.py
│   │           │   │   │   ├── response_input_param.py
│   │           │   │   │   ├── response_input_text.py
│   │           │   │   │   ├── response_input_text_param.py
│   │           │   │   │   ├── response_item.py
│   │           │   │   │   ├── response_item_list.py
│   │           │   │   │   ├── response_output_item.py
│   │           │   │   │   ├── response_output_item_added_event.py
│   │           │   │   │   ├── response_output_item_done_event.py
│   │           │   │   │   ├── response_output_message.py
│   │           │   │   │   ├── response_output_message_param.py
│   │           │   │   │   ├── response_output_refusal.py
│   │           │   │   │   ├── response_output_refusal_param.py
│   │           │   │   │   ├── response_output_text.py
│   │           │   │   │   ├── response_output_text_param.py
│   │           │   │   │   ├── response_reasoning_item.py
│   │           │   │   │   ├── response_reasoning_item_param.py
│   │           │   │   │   ├── response_refusal_delta_event.py
│   │           │   │   │   ├── response_refusal_done_event.py
│   │           │   │   │   ├── response_retrieve_params.py
│   │           │   │   │   ├── response_status.py
│   │           │   │   │   ├── response_stream_event.py
│   │           │   │   │   ├── response_text_annotation_delta_event.py
│   │           │   │   │   ├── response_text_config.py
│   │           │   │   │   ├── response_text_config_param.py
│   │           │   │   │   ├── response_text_delta_event.py
│   │           │   │   │   ├── response_text_done_event.py
│   │           │   │   │   ├── response_usage.py
│   │           │   │   │   ├── response_web_search_call_completed_event.py
│   │           │   │   │   ├── response_web_search_call_in_progress_event.py
│   │           │   │   │   ├── response_web_search_call_searching_event.py
│   │           │   │   │   ├── tool.py
│   │           │   │   │   ├── tool_choice_function.py
│   │           │   │   │   ├── tool_choice_function_param.py
│   │           │   │   │   ├── tool_choice_options.py
│   │           │   │   │   ├── tool_choice_types.py
│   │           │   │   │   ├── tool_choice_types_param.py
│   │           │   │   │   ├── tool_param.py
│   │           │   │   │   ├── web_search_tool.py
│   │           │   │   │   └── web_search_tool_param.py
│   │           │   │   ├── shared
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── all_models.py
│   │           │   │   │   ├── chat_model.py
│   │           │   │   │   ├── comparison_filter.py
│   │           │   │   │   ├── compound_filter.py
│   │           │   │   │   ├── error_object.py
│   │           │   │   │   ├── function_definition.py
│   │           │   │   │   ├── function_parameters.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── reasoning.py
│   │           │   │   │   ├── reasoning_effort.py
│   │           │   │   │   ├── response_format_json_object.py
│   │           │   │   │   ├── response_format_json_schema.py
│   │           │   │   │   ├── response_format_text.py
│   │           │   │   │   └── responses_model.py
│   │           │   │   ├── shared_params
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── chat_model.py
│   │           │   │   │   ├── comparison_filter.py
│   │           │   │   │   ├── compound_filter.py
│   │           │   │   │   ├── function_definition.py
│   │           │   │   │   ├── function_parameters.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── reasoning.py
│   │           │   │   │   ├── reasoning_effort.py
│   │           │   │   │   ├── response_format_json_object.py
│   │           │   │   │   ├── response_format_json_schema.py
│   │           │   │   │   ├── response_format_text.py
│   │           │   │   │   └── responses_model.py
│   │           │   │   ├── static_file_chunking_strategy.py
│   │           │   │   ├── static_file_chunking_strategy_object.py
│   │           │   │   ├── static_file_chunking_strategy_object_param.py
│   │           │   │   ├── static_file_chunking_strategy_param.py
│   │           │   │   ├── upload.py
│   │           │   │   ├── upload_complete_params.py
│   │           │   │   ├── upload_create_params.py
│   │           │   │   ├── uploads
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── part_create_params.py
│   │           │   │   │   └── upload_part.py
│   │           │   │   ├── vector_store.py
│   │           │   │   ├── vector_store_create_params.py
│   │           │   │   ├── vector_store_deleted.py
│   │           │   │   ├── vector_store_list_params.py
│   │           │   │   ├── vector_store_search_params.py
│   │           │   │   ├── vector_store_search_response.py
│   │           │   │   ├── vector_store_update_params.py
│   │           │   │   ├── vector_stores
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── file_batch_create_params.py
│   │           │   │   │   ├── file_batch_list_files_params.py
│   │           │   │   │   ├── file_content_response.py
│   │           │   │   │   ├── file_create_params.py
│   │           │   │   │   ├── file_list_params.py
│   │           │   │   │   ├── file_update_params.py
│   │           │   │   │   ├── vector_store_file.py
│   │           │   │   │   ├── vector_store_file_batch.py
│   │           │   │   │   └── vector_store_file_deleted.py
│   │           │   │   └── websocket_connection_options.py
│   │           │   └── version.py
│   │           ├── openai-1.69.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── packaging
│   │           │   ├── __init__.py
│   │           │   ├── _elffile.py
│   │           │   ├── _manylinux.py
│   │           │   ├── _musllinux.py
│   │           │   ├── _parser.py
│   │           │   ├── _structures.py
│   │           │   ├── _tokenizer.py
│   │           │   ├── licenses
│   │           │   │   ├── __init__.py
│   │           │   │   └── _spdx.py
│   │           │   ├── markers.py
│   │           │   ├── metadata.py
│   │           │   ├── py.typed
│   │           │   ├── requirements.py
│   │           │   ├── specifiers.py
│   │           │   ├── tags.py
│   │           │   ├── utils.py
│   │           │   └── version.py
│   │           ├── packaging-24.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── LICENSE.APACHE
│   │           │   ├── LICENSE.BSD
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── parse-1.20.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── parse.py
│   │           ├── parse_type
│   │           │   ├── __init__.py
│   │           │   ├── _version.py
│   │           │   ├── builder.py
│   │           │   ├── cardinality.py
│   │           │   ├── cardinality_field.py
│   │           │   ├── cfparse.py
│   │           │   ├── parse.py
│   │           │   └── parse_util.py
│   │           ├── parse_type-0.6.4.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── top_level.txt
│   │           │   └── zip-safe
│   │           ├── pathspec
│   │           │   ├── __init__.py
│   │           │   ├── _meta.py
│   │           │   ├── gitignore.py
│   │           │   ├── pathspec.py
│   │           │   ├── pattern.py
│   │           │   ├── patterns
│   │           │   │   ├── __init__.py
│   │           │   │   └── gitwildmatch.py
│   │           │   ├── py.typed
│   │           │   └── util.py
│   │           ├── pathspec-0.12.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   └── WHEEL
│   │           ├── pip
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── __pip-runner__.py
│   │           │   ├── _internal
│   │           │   │   ├── __init__.py
│   │           │   │   ├── build_env.py
│   │           │   │   ├── cache.py
│   │           │   │   ├── cli
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── autocompletion.py
│   │           │   │   │   ├── base_command.py
│   │           │   │   │   ├── cmdoptions.py
│   │           │   │   │   ├── command_context.py
│   │           │   │   │   ├── index_command.py
│   │           │   │   │   ├── main.py
│   │           │   │   │   ├── main_parser.py
│   │           │   │   │   ├── parser.py
│   │           │   │   │   ├── progress_bars.py
│   │           │   │   │   ├── req_command.py
│   │           │   │   │   ├── spinners.py
│   │           │   │   │   └── status_codes.py
│   │           │   │   ├── commands
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── completion.py
│   │           │   │   │   ├── configuration.py
│   │           │   │   │   ├── debug.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── hash.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── inspect.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   ├── list.py
│   │           │   │   │   ├── search.py
│   │           │   │   │   ├── show.py
│   │           │   │   │   ├── uninstall.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── configuration.py
│   │           │   │   ├── distributions
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── installed.py
│   │           │   │   │   ├── sdist.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── index
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── collector.py
│   │           │   │   │   ├── package_finder.py
│   │           │   │   │   └── sources.py
│   │           │   │   ├── locations
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _distutils.py
│   │           │   │   │   ├── _sysconfig.py
│   │           │   │   │   └── base.py
│   │           │   │   ├── main.py
│   │           │   │   ├── metadata
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _json.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── importlib
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _compat.py
│   │           │   │   │   │   ├── _dists.py
│   │           │   │   │   │   └── _envs.py
│   │           │   │   │   └── pkg_resources.py
│   │           │   │   ├── models
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── candidate.py
│   │           │   │   │   ├── direct_url.py
│   │           │   │   │   ├── format_control.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── installation_report.py
│   │           │   │   │   ├── link.py
│   │           │   │   │   ├── scheme.py
│   │           │   │   │   ├── search_scope.py
│   │           │   │   │   ├── selection_prefs.py
│   │           │   │   │   ├── target_python.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── network
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── lazy_wheel.py
│   │           │   │   │   ├── session.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── xmlrpc.py
│   │           │   │   ├── operations
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── install
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── editable_legacy.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   └── prepare.py
│   │           │   │   ├── pyproject.py
│   │           │   │   ├── req
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── constructors.py
│   │           │   │   │   ├── req_file.py
│   │           │   │   │   ├── req_install.py
│   │           │   │   │   ├── req_set.py
│   │           │   │   │   └── req_uninstall.py
│   │           │   │   ├── resolution
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── legacy
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   └── resolvelib
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── base.py
│   │           │   │   │       ├── candidates.py
│   │           │   │   │       ├── factory.py
│   │           │   │   │       ├── found_candidates.py
│   │           │   │   │       ├── provider.py
│   │           │   │   │       ├── reporter.py
│   │           │   │   │       ├── requirements.py
│   │           │   │   │       └── resolver.py
│   │           │   │   ├── self_outdated_check.py
│   │           │   │   ├── utils
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _jaraco_text.py
│   │           │   │   │   ├── _log.py
│   │           │   │   │   ├── appdirs.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── compatibility_tags.py
│   │           │   │   │   ├── datetime.py
│   │           │   │   │   ├── deprecation.py
│   │           │   │   │   ├── direct_url_helpers.py
│   │           │   │   │   ├── egg_link.py
│   │           │   │   │   ├── entrypoints.py
│   │           │   │   │   ├── filesystem.py
│   │           │   │   │   ├── filetypes.py
│   │           │   │   │   ├── glibc.py
│   │           │   │   │   ├── hashes.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── misc.py
│   │           │   │   │   ├── packaging.py
│   │           │   │   │   ├── retry.py
│   │           │   │   │   ├── setuptools_build.py
│   │           │   │   │   ├── subprocess.py
│   │           │   │   │   ├── temp_dir.py
│   │           │   │   │   ├── unpacking.py
│   │           │   │   │   ├── urls.py
│   │           │   │   │   ├── virtualenv.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── vcs
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── bazaar.py
│   │           │   │   │   ├── git.py
│   │           │   │   │   ├── mercurial.py
│   │           │   │   │   ├── subversion.py
│   │           │   │   │   └── versioncontrol.py
│   │           │   │   └── wheel_builder.py
│   │           │   ├── _vendor
│   │           │   │   ├── __init__.py
│   │           │   │   ├── cachecontrol
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _cmd.py
│   │           │   │   │   ├── adapter.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── caches
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── file_cache.py
│   │           │   │   │   │   └── redis_cache.py
│   │           │   │   │   ├── controller.py
│   │           │   │   │   ├── filewrapper.py
│   │           │   │   │   ├── heuristics.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── serialize.py
│   │           │   │   │   └── wrapper.py
│   │           │   │   ├── certifi
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── cacert.pem
│   │           │   │   │   ├── core.py
│   │           │   │   │   └── py.typed
│   │           │   │   ├── distlib
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── database.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── locators.py
│   │           │   │   │   ├── manifest.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── resources.py
│   │           │   │   │   ├── scripts.py
│   │           │   │   │   ├── t32.exe
│   │           │   │   │   ├── t64-arm.exe
│   │           │   │   │   ├── t64.exe
│   │           │   │   │   ├── util.py
│   │           │   │   │   ├── version.py
│   │           │   │   │   ├── w32.exe
│   │           │   │   │   ├── w64-arm.exe
│   │           │   │   │   ├── w64.exe
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── distro
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── distro.py
│   │           │   │   │   └── py.typed
│   │           │   │   ├── idna
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── codec.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── idnadata.py
│   │           │   │   │   ├── intranges.py
│   │           │   │   │   ├── package_data.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   └── uts46data.py
│   │           │   │   ├── msgpack
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── ext.py
│   │           │   │   │   └── fallback.py
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _elffile.py
│   │           │   │   │   ├── _manylinux.py
│   │           │   │   │   ├── _musllinux.py
│   │           │   │   │   ├── _parser.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── _tokenizer.py
│   │           │   │   │   ├── licenses
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _spdx.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── tags.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── pkg_resources
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── platformdirs
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── android.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── macos.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── unix.py
│   │           │   │   │   ├── version.py
│   │           │   │   │   └── windows.py
│   │           │   │   ├── pygments
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── cmdline.py
│   │           │   │   │   ├── console.py
│   │           │   │   │   ├── filter.py
│   │           │   │   │   ├── filters
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── formatter.py
│   │           │   │   │   ├── formatters
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _mapping.py
│   │           │   │   │   │   ├── bbcode.py
│   │           │   │   │   │   ├── groff.py
│   │           │   │   │   │   ├── html.py
│   │           │   │   │   │   ├── img.py
│   │           │   │   │   │   ├── irc.py
│   │           │   │   │   │   ├── latex.py
│   │           │   │   │   │   ├── other.py
│   │           │   │   │   │   ├── pangomarkup.py
│   │           │   │   │   │   ├── rtf.py
│   │           │   │   │   │   ├── svg.py
│   │           │   │   │   │   ├── terminal.py
│   │           │   │   │   │   └── terminal256.py
│   │           │   │   │   ├── lexer.py
│   │           │   │   │   ├── lexers
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _mapping.py
│   │           │   │   │   │   └── python.py
│   │           │   │   │   ├── modeline.py
│   │           │   │   │   ├── plugin.py
│   │           │   │   │   ├── regexopt.py
│   │           │   │   │   ├── scanner.py
│   │           │   │   │   ├── sphinxext.py
│   │           │   │   │   ├── style.py
│   │           │   │   │   ├── styles
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _mapping.py
│   │           │   │   │   ├── token.py
│   │           │   │   │   ├── unistring.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── pyproject_hooks
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _impl.py
│   │           │   │   │   ├── _in_process
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _in_process.py
│   │           │   │   │   └── py.typed
│   │           │   │   ├── requests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __version__.py
│   │           │   │   │   ├── _internal_utils.py
│   │           │   │   │   ├── adapters.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── certs.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── cookies.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── hooks.py
│   │           │   │   │   ├── models.py
│   │           │   │   │   ├── packages.py
│   │           │   │   │   ├── sessions.py
│   │           │   │   │   ├── status_codes.py
│   │           │   │   │   ├── structures.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── resolvelib
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── compat
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── collections_abc.py
│   │           │   │   │   ├── providers.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── reporters.py
│   │           │   │   │   ├── resolvers.py
│   │           │   │   │   └── structs.py
│   │           │   │   ├── rich
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __main__.py
│   │           │   │   │   ├── _cell_widths.py
│   │           │   │   │   ├── _emoji_codes.py
│   │           │   │   │   ├── _emoji_replace.py
│   │           │   │   │   ├── _export_format.py
│   │           │   │   │   ├── _extension.py
│   │           │   │   │   ├── _fileno.py
│   │           │   │   │   ├── _inspect.py
│   │           │   │   │   ├── _log_render.py
│   │           │   │   │   ├── _loop.py
│   │           │   │   │   ├── _null_file.py
│   │           │   │   │   ├── _palettes.py
│   │           │   │   │   ├── _pick.py
│   │           │   │   │   ├── _ratio.py
│   │           │   │   │   ├── _spinners.py
│   │           │   │   │   ├── _stack.py
│   │           │   │   │   ├── _timer.py
│   │           │   │   │   ├── _win32_console.py
│   │           │   │   │   ├── _windows.py
│   │           │   │   │   ├── _windows_renderer.py
│   │           │   │   │   ├── _wrap.py
│   │           │   │   │   ├── abc.py
│   │           │   │   │   ├── align.py
│   │           │   │   │   ├── ansi.py
│   │           │   │   │   ├── bar.py
│   │           │   │   │   ├── box.py
│   │           │   │   │   ├── cells.py
│   │           │   │   │   ├── color.py
│   │           │   │   │   ├── color_triplet.py
│   │           │   │   │   ├── columns.py
│   │           │   │   │   ├── console.py
│   │           │   │   │   ├── constrain.py
│   │           │   │   │   ├── containers.py
│   │           │   │   │   ├── control.py
│   │           │   │   │   ├── default_styles.py
│   │           │   │   │   ├── diagnose.py
│   │           │   │   │   ├── emoji.py
│   │           │   │   │   ├── errors.py
│   │           │   │   │   ├── file_proxy.py
│   │           │   │   │   ├── filesize.py
│   │           │   │   │   ├── highlighter.py
│   │           │   │   │   ├── json.py
│   │           │   │   │   ├── jupyter.py
│   │           │   │   │   ├── layout.py
│   │           │   │   │   ├── live.py
│   │           │   │   │   ├── live_render.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── markup.py
│   │           │   │   │   ├── measure.py
│   │           │   │   │   ├── padding.py
│   │           │   │   │   ├── pager.py
│   │           │   │   │   ├── palette.py
│   │           │   │   │   ├── panel.py
│   │           │   │   │   ├── pretty.py
│   │           │   │   │   ├── progress.py
│   │           │   │   │   ├── progress_bar.py
│   │           │   │   │   ├── prompt.py
│   │           │   │   │   ├── protocol.py
│   │           │   │   │   ├── py.typed
│   │           │   │   │   ├── region.py
│   │           │   │   │   ├── repr.py
│   │           │   │   │   ├── rule.py
│   │           │   │   │   ├── scope.py
│   │           │   │   │   ├── screen.py
│   │           │   │   │   ├── segment.py
│   │           │   │   │   ├── spinner.py
│   │           │   │   │   ├── status.py
│   │           │   │   │   ├── style.py
│   │           │   │   │   ├── styled.py
│   │           │   │   │   ├── syntax.py
│   │           │   │   │   ├── table.py
│   │           │   │   │   ├── terminal_theme.py
│   │           │   │   │   ├── text.py
│   │           │   │   │   ├── theme.py
│   │           │   │   │   ├── themes.py
│   │           │   │   │   ├── traceback.py
│   │           │   │   │   └── tree.py
│   │           │   │   ├── tomli
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _parser.py
│   │           │   │   │   ├── _re.py
│   │           │   │   │   ├── _types.py
│   │           │   │   │   └── py.typed
│   │           │   │   ├── truststore
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _api.py
│   │           │   │   │   ├── _macos.py
│   │           │   │   │   ├── _openssl.py
│   │           │   │   │   ├── _ssl_constants.py
│   │           │   │   │   ├── _windows.py
│   │           │   │   │   └── py.typed
│   │           │   │   ├── typing_extensions.py
│   │           │   │   ├── urllib3
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _collections.py
│   │           │   │   │   ├── _version.py
│   │           │   │   │   ├── connection.py
│   │           │   │   │   ├── connectionpool.py
│   │           │   │   │   ├── contrib
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _appengine_environ.py
│   │           │   │   │   │   ├── _securetransport
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── bindings.py
│   │           │   │   │   │   │   └── low_level.py
│   │           │   │   │   │   ├── appengine.py
│   │           │   │   │   │   ├── ntlmpool.py
│   │           │   │   │   │   ├── pyopenssl.py
│   │           │   │   │   │   ├── securetransport.py
│   │           │   │   │   │   └── socks.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── fields.py
│   │           │   │   │   ├── filepost.py
│   │           │   │   │   ├── packages
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── backports
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── makefile.py
│   │           │   │   │   │   │   └── weakref_finalize.py
│   │           │   │   │   │   └── six.py
│   │           │   │   │   ├── poolmanager.py
│   │           │   │   │   ├── request.py
│   │           │   │   │   ├── response.py
│   │           │   │   │   └── util
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── connection.py
│   │           │   │   │       ├── proxy.py
│   │           │   │   │       ├── queue.py
│   │           │   │   │       ├── request.py
│   │           │   │   │       ├── response.py
│   │           │   │   │       ├── retry.py
│   │           │   │   │       ├── ssl_.py
│   │           │   │   │       ├── ssl_match_hostname.py
│   │           │   │   │       ├── ssltransport.py
│   │           │   │   │       ├── timeout.py
│   │           │   │   │       ├── url.py
│   │           │   │   │       └── wait.py
│   │           │   │   └── vendor.txt
│   │           │   └── py.typed
│   │           ├── pip-25.0.1.dist-info
│   │           │   ├── AUTHORS.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── platformdirs
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── android.py
│   │           │   ├── api.py
│   │           │   ├── macos.py
│   │           │   ├── py.typed
│   │           │   ├── unix.py
│   │           │   ├── version.py
│   │           │   └── windows.py
│   │           ├── platformdirs-4.3.7.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── pluggy
│   │           │   ├── __init__.py
│   │           │   ├── _callers.py
│   │           │   ├── _hooks.py
│   │           │   ├── _manager.py
│   │           │   ├── _result.py
│   │           │   ├── _tracing.py
│   │           │   ├── _version.py
│   │           │   ├── _warnings.py
│   │           │   └── py.typed
│   │           ├── pluggy-1.5.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── pre_commit
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── all_languages.py
│   │           │   ├── clientlib.py
│   │           │   ├── color.py
│   │           │   ├── commands
│   │           │   │   ├── __init__.py
│   │           │   │   ├── autoupdate.py
│   │           │   │   ├── clean.py
│   │           │   │   ├── gc.py
│   │           │   │   ├── hook_impl.py
│   │           │   │   ├── init_templatedir.py
│   │           │   │   ├── install_uninstall.py
│   │           │   │   ├── migrate_config.py
│   │           │   │   ├── run.py
│   │           │   │   ├── sample_config.py
│   │           │   │   ├── try_repo.py
│   │           │   │   ├── validate_config.py
│   │           │   │   └── validate_manifest.py
│   │           │   ├── constants.py
│   │           │   ├── envcontext.py
│   │           │   ├── error_handler.py
│   │           │   ├── errors.py
│   │           │   ├── file_lock.py
│   │           │   ├── git.py
│   │           │   ├── hook.py
│   │           │   ├── lang_base.py
│   │           │   ├── languages
│   │           │   │   ├── __init__.py
│   │           │   │   ├── conda.py
│   │           │   │   ├── coursier.py
│   │           │   │   ├── dart.py
│   │           │   │   ├── docker.py
│   │           │   │   ├── docker_image.py
│   │           │   │   ├── dotnet.py
│   │           │   │   ├── fail.py
│   │           │   │   ├── golang.py
│   │           │   │   ├── haskell.py
│   │           │   │   ├── julia.py
│   │           │   │   ├── lua.py
│   │           │   │   ├── node.py
│   │           │   │   ├── perl.py
│   │           │   │   ├── pygrep.py
│   │           │   │   ├── python.py
│   │           │   │   ├── r.py
│   │           │   │   ├── ruby.py
│   │           │   │   ├── rust.py
│   │           │   │   ├── script.py
│   │           │   │   ├── swift.py
│   │           │   │   └── system.py
│   │           │   ├── logging_handler.py
│   │           │   ├── main.py
│   │           │   ├── meta_hooks
│   │           │   │   ├── __init__.py
│   │           │   │   ├── check_hooks_apply.py
│   │           │   │   ├── check_useless_excludes.py
│   │           │   │   └── identity.py
│   │           │   ├── output.py
│   │           │   ├── parse_shebang.py
│   │           │   ├── prefix.py
│   │           │   ├── repository.py
│   │           │   ├── resources
│   │           │   │   ├── __init__.py
│   │           │   │   ├── empty_template_.npmignore
│   │           │   │   ├── empty_template_Cargo.toml
│   │           │   │   ├── empty_template_LICENSE.renv
│   │           │   │   ├── empty_template_Makefile.PL
│   │           │   │   ├── empty_template_activate.R
│   │           │   │   ├── empty_template_environment.yml
│   │           │   │   ├── empty_template_go.mod
│   │           │   │   ├── empty_template_main.go
│   │           │   │   ├── empty_template_main.rs
│   │           │   │   ├── empty_template_package.json
│   │           │   │   ├── empty_template_pre-commit-package-dev-1.rockspec
│   │           │   │   ├── empty_template_pre_commit_placeholder_package.gemspec
│   │           │   │   ├── empty_template_pubspec.yaml
│   │           │   │   ├── empty_template_renv.lock
│   │           │   │   ├── empty_template_setup.py
│   │           │   │   ├── hook-tmpl
│   │           │   │   ├── rbenv.tar.gz
│   │           │   │   ├── ruby-build.tar.gz
│   │           │   │   └── ruby-download.tar.gz
│   │           │   ├── staged_files_only.py
│   │           │   ├── store.py
│   │           │   ├── util.py
│   │           │   ├── xargs.py
│   │           │   ├── yaml.py
│   │           │   └── yaml_rewrite.py
│   │           ├── pre_commit-4.2.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── py.py
│   │           ├── pydantic
│   │           │   ├── __init__.py
│   │           │   ├── _internal
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _config.py
│   │           │   │   ├── _core_metadata.py
│   │           │   │   ├── _core_utils.py
│   │           │   │   ├── _dataclasses.py
│   │           │   │   ├── _decorators.py
│   │           │   │   ├── _decorators_v1.py
│   │           │   │   ├── _discriminated_union.py
│   │           │   │   ├── _docs_extraction.py
│   │           │   │   ├── _fields.py
│   │           │   │   ├── _forward_ref.py
│   │           │   │   ├── _generate_schema.py
│   │           │   │   ├── _generics.py
│   │           │   │   ├── _git.py
│   │           │   │   ├── _import_utils.py
│   │           │   │   ├── _internal_dataclass.py
│   │           │   │   ├── _known_annotated_metadata.py
│   │           │   │   ├── _mock_val_ser.py
│   │           │   │   ├── _model_construction.py
│   │           │   │   ├── _namespace_utils.py
│   │           │   │   ├── _repr.py
│   │           │   │   ├── _schema_gather.py
│   │           │   │   ├── _schema_generation_shared.py
│   │           │   │   ├── _serializers.py
│   │           │   │   ├── _signature.py
│   │           │   │   ├── _typing_extra.py
│   │           │   │   ├── _utils.py
│   │           │   │   ├── _validate_call.py
│   │           │   │   └── _validators.py
│   │           │   ├── _migration.py
│   │           │   ├── alias_generators.py
│   │           │   ├── aliases.py
│   │           │   ├── annotated_handlers.py
│   │           │   ├── class_validators.py
│   │           │   ├── color.py
│   │           │   ├── config.py
│   │           │   ├── dataclasses.py
│   │           │   ├── datetime_parse.py
│   │           │   ├── decorator.py
│   │           │   ├── deprecated
│   │           │   │   ├── __init__.py
│   │           │   │   ├── class_validators.py
│   │           │   │   ├── config.py
│   │           │   │   ├── copy_internals.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── json.py
│   │           │   │   ├── parse.py
│   │           │   │   └── tools.py
│   │           │   ├── env_settings.py
│   │           │   ├── error_wrappers.py
│   │           │   ├── errors.py
│   │           │   ├── experimental
│   │           │   │   ├── __init__.py
│   │           │   │   ├── arguments_schema.py
│   │           │   │   └── pipeline.py
│   │           │   ├── fields.py
│   │           │   ├── functional_serializers.py
│   │           │   ├── functional_validators.py
│   │           │   ├── generics.py
│   │           │   ├── json.py
│   │           │   ├── json_schema.py
│   │           │   ├── main.py
│   │           │   ├── mypy.py
│   │           │   ├── networks.py
│   │           │   ├── parse.py
│   │           │   ├── plugin
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _loader.py
│   │           │   │   └── _schema_validator.py
│   │           │   ├── py.typed
│   │           │   ├── root_model.py
│   │           │   ├── schema.py
│   │           │   ├── tools.py
│   │           │   ├── type_adapter.py
│   │           │   ├── types.py
│   │           │   ├── typing.py
│   │           │   ├── utils.py
│   │           │   ├── v1
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _hypothesis_plugin.py
│   │           │   │   ├── annotated_types.py
│   │           │   │   ├── class_validators.py
│   │           │   │   ├── color.py
│   │           │   │   ├── config.py
│   │           │   │   ├── dataclasses.py
│   │           │   │   ├── datetime_parse.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── env_settings.py
│   │           │   │   ├── error_wrappers.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── fields.py
│   │           │   │   ├── generics.py
│   │           │   │   ├── json.py
│   │           │   │   ├── main.py
│   │           │   │   ├── mypy.py
│   │           │   │   ├── networks.py
│   │           │   │   ├── parse.py
│   │           │   │   ├── py.typed
│   │           │   │   ├── schema.py
│   │           │   │   ├── tools.py
│   │           │   │   ├── types.py
│   │           │   │   ├── typing.py
│   │           │   │   ├── utils.py
│   │           │   │   ├── validators.py
│   │           │   │   └── version.py
│   │           │   ├── validate_call_decorator.py
│   │           │   ├── validators.py
│   │           │   ├── version.py
│   │           │   └── warnings.py
│   │           ├── pydantic-2.11.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── pydantic_core
│   │           │   ├── __init__.py
│   │           │   ├── _pydantic_core.cpython-312-darwin.so
│   │           │   ├── _pydantic_core.pyi
│   │           │   ├── core_schema.py
│   │           │   └── py.typed
│   │           ├── pydantic_core-2.33.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── pytest
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── py.typed
│   │           ├── pytest-8.3.5.dist-info
│   │           │   ├── AUTHORS
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── requests
│   │           │   ├── __init__.py
│   │           │   ├── __version__.py
│   │           │   ├── _internal_utils.py
│   │           │   ├── adapters.py
│   │           │   ├── api.py
│   │           │   ├── auth.py
│   │           │   ├── certs.py
│   │           │   ├── compat.py
│   │           │   ├── cookies.py
│   │           │   ├── exceptions.py
│   │           │   ├── help.py
│   │           │   ├── hooks.py
│   │           │   ├── models.py
│   │           │   ├── packages.py
│   │           │   ├── sessions.py
│   │           │   ├── status_codes.py
│   │           │   ├── structures.py
│   │           │   └── utils.py
│   │           ├── requests-2.32.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── setuptools_behave.py
│   │           ├── six-1.17.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── six.py
│   │           ├── sniffio
│   │           │   ├── __init__.py
│   │           │   ├── _impl.py
│   │           │   ├── _tests
│   │           │   │   ├── __init__.py
│   │           │   │   └── test_sniffio.py
│   │           │   ├── _version.py
│   │           │   └── py.typed
│   │           ├── sniffio-1.3.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── LICENSE.APACHE2
│   │           │   ├── LICENSE.MIT
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── top_level.txt
│   │           ├── starlette
│   │           │   ├── __init__.py
│   │           │   ├── _exception_handler.py
│   │           │   ├── _utils.py
│   │           │   ├── applications.py
│   │           │   ├── authentication.py
│   │           │   ├── background.py
│   │           │   ├── concurrency.py
│   │           │   ├── config.py
│   │           │   ├── convertors.py
│   │           │   ├── datastructures.py
│   │           │   ├── endpoints.py
│   │           │   ├── exceptions.py
│   │           │   ├── formparsers.py
│   │           │   ├── middleware
│   │           │   │   ├── __init__.py
│   │           │   │   ├── authentication.py
│   │           │   │   ├── base.py
│   │           │   │   ├── cors.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── gzip.py
│   │           │   │   ├── httpsredirect.py
│   │           │   │   ├── sessions.py
│   │           │   │   ├── trustedhost.py
│   │           │   │   └── wsgi.py
│   │           │   ├── py.typed
│   │           │   ├── requests.py
│   │           │   ├── responses.py
│   │           │   ├── routing.py
│   │           │   ├── schemas.py
│   │           │   ├── staticfiles.py
│   │           │   ├── status.py
│   │           │   ├── templating.py
│   │           │   ├── testclient.py
│   │           │   ├── types.py
│   │           │   └── websockets.py
│   │           ├── starlette-0.46.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE.md
│   │           ├── tqdm
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _dist_ver.py
│   │           │   ├── _main.py
│   │           │   ├── _monitor.py
│   │           │   ├── _tqdm.py
│   │           │   ├── _tqdm_gui.py
│   │           │   ├── _tqdm_notebook.py
│   │           │   ├── _tqdm_pandas.py
│   │           │   ├── _utils.py
│   │           │   ├── asyncio.py
│   │           │   ├── auto.py
│   │           │   ├── autonotebook.py
│   │           │   ├── cli.py
│   │           │   ├── completion.sh
│   │           │   ├── contrib
│   │           │   │   ├── __init__.py
│   │           │   │   ├── bells.py
│   │           │   │   ├── concurrent.py
│   │           │   │   ├── discord.py
│   │           │   │   ├── itertools.py
│   │           │   │   ├── logging.py
│   │           │   │   ├── slack.py
│   │           │   │   ├── telegram.py
│   │           │   │   └── utils_worker.py
│   │           │   ├── dask.py
│   │           │   ├── gui.py
│   │           │   ├── keras.py
│   │           │   ├── notebook.py
│   │           │   ├── rich.py
│   │           │   ├── std.py
│   │           │   ├── tk.py
│   │           │   ├── tqdm.1
│   │           │   ├── utils.py
│   │           │   └── version.py
│   │           ├── tqdm-4.67.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENCE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── top_level.txt
│   │           ├── typing_extensions-4.13.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── typing_extensions.py
│   │           ├── typing_inspection
│   │           │   ├── __init__.py
│   │           │   ├── introspection.py
│   │           │   ├── py.typed
│   │           │   ├── typing_objects.py
│   │           │   └── typing_objects.pyi
│   │           ├── typing_inspection-0.4.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           ├── urllib3
│   │           │   ├── __init__.py
│   │           │   ├── _base_connection.py
│   │           │   ├── _collections.py
│   │           │   ├── _request_methods.py
│   │           │   ├── _version.py
│   │           │   ├── connection.py
│   │           │   ├── connectionpool.py
│   │           │   ├── contrib
│   │           │   │   ├── __init__.py
│   │           │   │   ├── emscripten
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── connection.py
│   │           │   │   │   ├── emscripten_fetch_worker.js
│   │           │   │   │   ├── fetch.py
│   │           │   │   │   ├── request.py
│   │           │   │   │   └── response.py
│   │           │   │   ├── pyopenssl.py
│   │           │   │   └── socks.py
│   │           │   ├── exceptions.py
│   │           │   ├── fields.py
│   │           │   ├── filepost.py
│   │           │   ├── http2
│   │           │   │   ├── __init__.py
│   │           │   │   ├── connection.py
│   │           │   │   └── probe.py
│   │           │   ├── poolmanager.py
│   │           │   ├── py.typed
│   │           │   ├── response.py
│   │           │   └── util
│   │           │       ├── __init__.py
│   │           │       ├── connection.py
│   │           │       ├── proxy.py
│   │           │       ├── request.py
│   │           │       ├── response.py
│   │           │       ├── retry.py
│   │           │       ├── ssl_.py
│   │           │       ├── ssl_match_hostname.py
│   │           │       ├── ssltransport.py
│   │           │       ├── timeout.py
│   │           │       ├── url.py
│   │           │       ├── util.py
│   │           │       └── wait.py
│   │           ├── urllib3-2.3.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   └── licenses
│   │           │       └── LICENSE.txt
│   │           ├── uvicorn
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── _subprocess.py
│   │           │   ├── _types.py
│   │           │   ├── config.py
│   │           │   ├── importer.py
│   │           │   ├── lifespan
│   │           │   │   ├── __init__.py
│   │           │   │   ├── off.py
│   │           │   │   └── on.py
│   │           │   ├── logging.py
│   │           │   ├── loops
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asyncio.py
│   │           │   │   ├── auto.py
│   │           │   │   └── uvloop.py
│   │           │   ├── main.py
│   │           │   ├── middleware
│   │           │   │   ├── __init__.py
│   │           │   │   ├── asgi2.py
│   │           │   │   ├── message_logger.py
│   │           │   │   ├── proxy_headers.py
│   │           │   │   └── wsgi.py
│   │           │   ├── protocols
│   │           │   │   ├── __init__.py
│   │           │   │   ├── http
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── auto.py
│   │           │   │   │   ├── flow_control.py
│   │           │   │   │   ├── h11_impl.py
│   │           │   │   │   └── httptools_impl.py
│   │           │   │   ├── utils.py
│   │           │   │   └── websockets
│   │           │   │       ├── __init__.py
│   │           │   │       ├── auto.py
│   │           │   │       ├── websockets_impl.py
│   │           │   │       └── wsproto_impl.py
│   │           │   ├── py.typed
│   │           │   ├── server.py
│   │           │   ├── supervisors
│   │           │   │   ├── __init__.py
│   │           │   │   ├── basereload.py
│   │           │   │   ├── multiprocess.py
│   │           │   │   ├── statreload.py
│   │           │   │   └── watchfilesreload.py
│   │           │   └── workers.py
│   │           ├── uvicorn-0.34.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE.md
│   │           ├── virtualenv
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   ├── activation
│   │           │   │   ├── __init__.py
│   │           │   │   ├── activator.py
│   │           │   │   ├── bash
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate.sh
│   │           │   │   ├── batch
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── activate.bat
│   │           │   │   │   ├── deactivate.bat
│   │           │   │   │   └── pydoc.bat
│   │           │   │   ├── cshell
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate.csh
│   │           │   │   ├── fish
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate.fish
│   │           │   │   ├── nushell
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate.nu
│   │           │   │   ├── powershell
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate.ps1
│   │           │   │   ├── python
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── activate_this.py
│   │           │   │   └── via_template.py
│   │           │   ├── app_data
│   │           │   │   ├── __init__.py
│   │           │   │   ├── base.py
│   │           │   │   ├── na.py
│   │           │   │   ├── read_only.py
│   │           │   │   ├── via_disk_folder.py
│   │           │   │   └── via_tempdir.py
│   │           │   ├── config
│   │           │   │   ├── __init__.py
│   │           │   │   ├── cli
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── parser.py
│   │           │   │   ├── convert.py
│   │           │   │   ├── env_var.py
│   │           │   │   └── ini.py
│   │           │   ├── create
│   │           │   │   ├── __init__.py
│   │           │   │   ├── creator.py
│   │           │   │   ├── debug.py
│   │           │   │   ├── describe.py
│   │           │   │   ├── pyenv_cfg.py
│   │           │   │   └── via_global_ref
│   │           │   │       ├── __init__.py
│   │           │   │       ├── _virtualenv.py
│   │           │   │       ├── api.py
│   │           │   │       ├── builtin
│   │           │   │       │   ├── __init__.py
│   │           │   │       │   ├── builtin_way.py
│   │           │   │       │   ├── cpython
│   │           │   │       │   │   ├── __init__.py
│   │           │   │       │   │   ├── common.py
│   │           │   │       │   │   ├── cpython3.py
│   │           │   │       │   │   └── mac_os.py
│   │           │   │       │   ├── pypy
│   │           │   │       │   │   ├── __init__.py
│   │           │   │       │   │   ├── common.py
│   │           │   │       │   │   └── pypy3.py
│   │           │   │       │   ├── ref.py
│   │           │   │       │   └── via_global_self_do.py
│   │           │   │       ├── store.py
│   │           │   │       └── venv.py
│   │           │   ├── discovery
│   │           │   │   ├── __init__.py
│   │           │   │   ├── builtin.py
│   │           │   │   ├── cached_py_info.py
│   │           │   │   ├── discover.py
│   │           │   │   ├── py_info.py
│   │           │   │   ├── py_spec.py
│   │           │   │   └── windows
│   │           │   │       ├── __init__.py
│   │           │   │       └── pep514.py
│   │           │   ├── info.py
│   │           │   ├── report.py
│   │           │   ├── run
│   │           │   │   ├── __init__.py
│   │           │   │   ├── plugin
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── activators.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── creators.py
│   │           │   │   │   ├── discovery.py
│   │           │   │   │   └── seeders.py
│   │           │   │   └── session.py
│   │           │   ├── seed
│   │           │   │   ├── __init__.py
│   │           │   │   ├── embed
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── base_embed.py
│   │           │   │   │   ├── pip_invoke.py
│   │           │   │   │   └── via_app_data
│   │           │   │   │       ├── __init__.py
│   │           │   │   │       ├── pip_install
│   │           │   │   │       │   ├── __init__.py
│   │           │   │   │       │   ├── base.py
│   │           │   │   │       │   ├── copy.py
│   │           │   │   │       │   └── symlink.py
│   │           │   │   │       └── via_app_data.py
│   │           │   │   ├── seeder.py
│   │           │   │   └── wheels
│   │           │   │       ├── __init__.py
│   │           │   │       ├── acquire.py
│   │           │   │       ├── bundle.py
│   │           │   │       ├── embed
│   │           │   │       │   ├── __init__.py
│   │           │   │       │   ├── pip-25.0.1-py3-none-any.whl
│   │           │   │       │   ├── setuptools-75.3.0-py3-none-any.whl
│   │           │   │       │   ├── setuptools-75.8.0-py3-none-any.whl
│   │           │   │       │   └── wheel-0.45.1-py3-none-any.whl
│   │           │   │       ├── periodic_update.py
│   │           │   │       └── util.py
│   │           │   ├── util
│   │           │   │   ├── __init__.py
│   │           │   │   ├── error.py
│   │           │   │   ├── lock.py
│   │           │   │   ├── path
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _permission.py
│   │           │   │   │   ├── _sync.py
│   │           │   │   │   └── _win.py
│   │           │   │   ├── subprocess
│   │           │   │   │   └── __init__.py
│   │           │   │   └── zipapp.py
│   │           │   └── version.py
│   │           ├── virtualenv-20.29.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── WHEEL
│   │           │   ├── entry_points.txt
│   │           │   └── licenses
│   │           │       └── LICENSE
│   │           └── yaml
│   │               ├── __init__.py
│   │               ├── _yaml.cpython-312-darwin.so
│   │               ├── composer.py
│   │               ├── constructor.py
│   │               ├── cyaml.py
│   │               ├── dumper.py
│   │               ├── emitter.py
│   │               ├── error.py
│   │               ├── events.py
│   │               ├── loader.py
│   │               ├── nodes.py
│   │               ├── parser.py
│   │               ├── reader.py
│   │               ├── representer.py
│   │               ├── resolver.py
│   │               ├── scanner.py
│   │               ├── serializer.py
│   │               └── tokens.py
│   └── pyvenv.cfg
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── config
│   └── settings.yaml
├── docs
│   ├── README.md
│   ├── app_requirements.md
│   ├── architecture.md
│   ├── bitwise_seed_yyyymmdd.json
│   ├── gitflow.md
│   ├── llm_integration.md
│   ├── philosophy.md
│   ├── previous
│   │   └── project_structure_20250329_014213.md
│   ├── project_structure.md
│   └── sequence.md
├── logs
│   ├── README.md
│   ├── api.log
│   └── app.log
├── requirements.txt
├── scripts
│   ├── README.md
│   ├── generate_project_structure_tree.py
│   ├── record_directory_listing.py
│   ├── rename_project.py
│   ├── rotate_logs.py
│   └── seed_init.py
├── seeds
│   ├── logimus_seed.json
│   ├── schematicus_seed.json
│   └── starter_assistant_seed.json
├── src
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   └── file_record.py
│   │   └── routes
│   │       └── scan.py
│   ├── cli
│   ├── core
│   │   └── scanner.py
│   ├── logging
│   │   ├── logging_config.yaml
│   │   └── setup_logging.py
│   ├── orchestration
│   │   ├── logimus_agent.py
│   │   └── schematicus_agent.py
│   ├── template_python_file.py
│   ├── ui
│   └── utils
│       └── config_loader.py
└── tests
    ├── README.md
    ├── __init__.py
    ├── features
    │   ├── environment.py
    │   ├── sample.feature
    │   ├── scan.feature
    │   └── steps
    │       ├── sample_steps.py
    │       └── test_scan.py
    ├── resources
    │   └── pictures_scan_baseline.json
    ├── test_scan_api.py
    └── test_smoke.py
```