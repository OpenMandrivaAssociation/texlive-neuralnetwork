%global tl_name neuralnetwork
%global tl_revision 31500

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Graph-drawing for neural networks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/neuralnetwork
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/neuralnetwork.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/neuralnetwork.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides facilities for graph-drawing, with facilities
designed for neural network diagrams.

