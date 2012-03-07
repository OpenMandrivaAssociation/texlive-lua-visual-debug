# revision 25517
# category Package
# catalog-ctan /macros/luatex/generic/lua-visual-debug
# catalog-date 2012-02-26 08:44:52 +0100
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-lua-visual-debug
Version:	0.1
Release:	1
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
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.tex
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.tex
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.pdf
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
