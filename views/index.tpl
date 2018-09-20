% rebase('main')
<h1>The News!</h1>
% c = 1
% for i in frettir:
    <a href="/{{c}}">{{i[0]}}</a>
% c += 1
%end
