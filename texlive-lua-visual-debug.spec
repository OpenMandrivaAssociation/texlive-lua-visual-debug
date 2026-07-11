%global tl_name lua-visual-debug
%global tl_revision 78797

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Visual debugging with LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/lua-visual-debug
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-visual-debug.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-visual-debug.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(luakeyval)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses lua code to provide visible indications of boxes,
glues, kerns and penalties in the PDF output. The package is known to
work in LaTeX and Plain TeX documents.

