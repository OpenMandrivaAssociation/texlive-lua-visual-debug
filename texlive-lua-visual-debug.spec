# revision 25881
# category Package
# catalog-ctan /macros/luatex/generic/lua-visual-debug
# catalog-date 2012-04-08 13:49:02 +0200
# catalog-license other-free
# catalog-version 0.4
Name:		texlive-lua-visual-debug
Version:	0.4
Release:	4
Summary:	Visual debugging with LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/lua-visual-debug
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-visual-debug.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-visual-debug.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses lua code to provide visible indications of
boxes, glues, kerns and penalties in the PDF output. The
package is known to work in LaTeX and Plain TeX documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/lua-visual-debug/lua-visual-debug.lua
%{_texmfdistdir}/tex/luatex/lua-visual-debug/lua-visual-debug.sty
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/README
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/README.doc
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.tex
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebugdetail1-num.png
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.tex
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.tex
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/strut.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 790648
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 787685
- Update to latest release.

* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 783050
- Import texlive-lua-visual-debug
- Import texlive-lua-visual-debug

