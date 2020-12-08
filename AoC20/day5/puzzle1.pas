program Puzzle1;

uses
  Math;

var
  InFile: Text;
  Line: string;
  MaxID, LineID: word;

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
  const
    RowCodeLen = 7;
    ColCodeLen = 3;
  var
    RowCode, ColCode: string;
  begin
    RowCode := Copy(Line, 1, RowCodeLen);
    ColCode := Copy(Line, 8, ColCodeLen);
    Result := GetPosition(RowCode, 0, Round(Power(2, RowCodeLen)) - 1, 'F', 'R') *
      8 + GetPosition(ColCode, 0, Round(Power(2, ColCodeLen)) - 1, 'L', 'R');
  end;

begin
  MaxID := 0;
  Assign(InFile, 'Input.txt');
  Reset(InFile);
  repeat
    ReadLn(InFile, Line);
    LineID := GetLineID(Line);
    if LineID > MaxID then
      MaxID := LineID;
  until EOF(InFile);
  Close(InFile);
  WriteLn(MaxID);
end.
