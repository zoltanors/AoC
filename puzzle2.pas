program Puzzle2;

uses
  Math;

const
  RowCodeLen = 7;
  ColCodeLen = 3;
  (* aka Power(2, (RowCodeLen + ColCodeLen)),
     but that is now working in constant declaration. *)
  NoSeats = 1 << (RowCodeLen + ColCodeLen);

var
  InFile: Text;
  Line: string;
  I: word;
  Seats: array[1..NoSeats] of boolean;

  function GetPosition(PosID: string; Min: word; Max: word; LowerChar: char;
    UpperChar: char): word;
  var
    NewPosID: string;
    NewMin, NewMax: word;
  begin
    if Length(PosID) = 1 then
      if PosID[1] = LowerChar then
        Result := Min
      else
        Result := Max
    else
    begin
      NewPosID := Copy(PosID, 2, Length(PosID) - 1);
      if PosID[1] = LowerChar then
      begin
        NewMin := Min;
        NewMax := Min + (Max - Min) div 2;
      end
      else
      begin
        NewMin := Max - (Max - Min) div 2;
        NewMax := Max;
      end;
      Result := GetPosition(NewPosID, NewMin, NewMax, LowerChar, UpperChar);
    end;
  end;

  function GetLineID(Line: string): word;
  var
    RowCode, ColCode: string;
  begin
    RowCode := Copy(Line, 1, RowCodeLen);
    ColCode := Copy(Line, 8, ColCodeLen);
    Result := GetPosition(RowCode, 0, Round(Power(2, RowCodeLen)) - 1, 'F', 'R') *
      8 + GetPosition(ColCode, 0, Round(Power(2, ColCodeLen)) - 1, 'L', 'R');
  end;

begin
  for I := 0 to NoSeats do
    Seats[I] := False;
  Assign(InFile, 'Input.txt');
  Reset(InFile);
  repeat
    ReadLn(InFile, Line);
    Seats[GetLineID(Line)] := True;
  until EOF(InFile);
  Close(InFile);
  for I := 1 to NoSeats - 1 do
    if Seats[I - 1] and not Seats[I] and Seats[I + 1] then
      WriteLn(I);
end.
