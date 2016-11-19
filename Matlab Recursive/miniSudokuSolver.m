function solved = miniSudokuSolver(sud)
% Solves Sudoku recursively! Input is a 9x9 grid with zeros as spaces.
% Josip S - 11/11/13. Man, I should be studying.

% If it's empty, return.
if isempty(sud), solved = []; return, end

% Returns the indicies where we can guess/put in numbers.
[i, j] = find(sud == 0);

% If there are no empty squares, we're done!
if isempty(i),solved = sud; return,end

% Has no result by default.
solved = [];

% Finds a good square spot to start guessing! (<=2 is good.)
% gridposs = the remaining numbers it could be from the numbers in the
% 3x3 grid. horzVertPos = the remaining numbers it could be numbers above/below
% and beside the ith and jth square. allPoss is the common numbers of these two.
for leastGuessIndx = 1:length(i)
    
    % Old code
    % gridposs = setxor(sud(ceil(i(leastGuessIndx)/3)*3-2:ceil(i(leastGuessIndx)/3)*3, ceil(j(leastGuessIndx)/3)*3-2:ceil(j(leastGuessIndx)/3)*3), (0:9));
    % horzVertPoss = intersect(setxor(sud(i(leastGuessIndx), :),(0:9)), setxor(sud(:, j(leastGuessIndx)),(0:9)));
    % allGuesses = intersect(gridposs, horzVertPoss)';
    
    % New code equivalent. (~14x faster, no setxoring.)
    gridposs = reshape(sud(ceil(i(leastGuessIndx)/3)*3-2:ceil(i(leastGuessIndx)/3)*3, ceil(j(leastGuessIndx)/3)*3-2:ceil(j(leastGuessIndx)/3)*3), 1, 9);
    horzVertPoss = [sud(i(leastGuessIndx), :) sud(:, j(leastGuessIndx))']; set=(0:9);
    allGuesses = set(~ismember(set, [gridposs horzVertPoss]));
    
    if isempty(allGuesses), return, end     % If any 0 has no possible moves, there's a contradiction.
    if length(allGuesses) <= 2, break, end  % If there are less that 2 valid guesses, use that.
end

% Takes a guess from each of the valid possibilities. Recursively calls
% itself on the new guess.
for guess = allGuesses
    sud(i(leastGuessIndx), j(leastGuessIndx)) = guess;
    result = miniSudokuSolver(sud);
    if ~isempty(result), solved = result; return; end
end
end
