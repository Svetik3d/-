//
var
    filetext, file_OUT: text;
    s_file, e_s, y_s:string;
    //i:integer;
    a,b: array[1..5] of integer;
    i, j,M: byte;
    f: boolean;
    n, number, e, y, final_n, final_e, final_y: integer;
    //check_len: boolean;
    function check(s:string):boolean;
    begin
        n:=length(s);
        for i:=1 to n do a[i]:=ord(s[i])-ord('0');//записываем массив
        i:=0;
        b[1] := a[1];
        M := 1;
        for i:=2 to n do begin
            f := true;
            for j:=1 to M do
                if a[i] = b[j] then 
                    f := false;
            if f = true then begin
                M := M + 1;
                b[M] := a[i];
            end;
        end;
        if M <= 2 then check:=true
        else check:=false;
    end;
begin
    assign(filetext,'./INPUT.txt');
    reset(filetext);
    readln(filetext, s_file);
    close(filetext);
    val(s_file, number);
    // ищем двоякое БОЛЬШЕЕ число
    for e:=number to 30000 do begin
        str(e, e_s);
        //writeln(i_s);
        if check(e_s) = true then begin
            final_e:=e;
            break;
        end;
    end;
    // ищем двоякое МЕНЬШЕЕ число
    for y:=number downto 1 do begin
        str(y, y_s);
        //writeln(i_s);
        if check(y_s) = true then begin
            final_y:=y;
            break;
        end;
    end;
    // ищем БЛИЖАЙШЕЕ двоякое число
    if (number-final_y) > (final_e-number) then final_n:=e
    else final_n:=y;
    assign(file_OUT, './OUTPUT.txt');
    rewrite(file_OUT);
    writeln(file_OUT, final_n);   
    close(file_OUT);
end.
