Name:		texlive-lua-visual-debug
Version:	0.7
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
%{_texmfdistdir}/tex/luatex/lua-visual-debug
%doc %{_texmfdistdir}/doc/luatex/lua-visual-debug

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
