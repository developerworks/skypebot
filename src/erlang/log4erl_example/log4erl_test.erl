%% Author: Administrator
%% Created: 2011-5-16
%% Description: TODO: Add description to log4erl_test
-module(log4erl_test).

%%
%% Include files
%%

%%
%% Exported Functions
%%
-export([start/0]).

%%
%% API Functions
%%



%%
%% Local Functions
%%

%% Testing the log4erl
start() ->
	application:start(log4erl),
	log4erl:conf("log4erl.conf"),
%% 	log4erl:add_logger(messages_log),
%% 	log4erl:add_console_appender(messages_log, cmd_logs, {error, "[%L] %l%n"}),
	log4erl:info("Database is connected."),
	ok.