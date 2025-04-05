%% 
%% This is file `a0poster.cls'
%% 
%% Copyright (C) 1997-2004 Gerlinde Kettl and Matthias Weiser
%%
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.2
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%% � �http://www.latex-project.org/lppl.txt
%% and version 1.2 or later is part of all distributions of LaTeX
%% version 1999/12/01 or later.
%%
%% Problems, bugs and comments to 
%% tex@kettl.de
%% 

\ProvidesClass{a0poster}[2004/01/31 v1.22b a0poster class (GK, MW)]
\NeedsTeXFormat{LaTeX2e}[1995/06/01]
\LoadClass{article}

\newif\ifportrait
\newif\ifanullb
\newif\ifanull
\newif\ifaeins
\newif\ifazwei
\newif\ifadrei
\newif\ifposterdraft

\newcount\xkoord
\newcount\ykoord
\newcount\xscale
\newcount\yscale

\DeclareOption{a0}{
\xkoord=2380 % big points (1 bp=1/72 inch)
\ykoord=3368 % big points (1 bp=1/72 inch)
\xscale=2
\yscale=2
}
\DeclareOption{landscape}{
\portraitfalse
}
\DeclareOption{portrait}{
\portraittrue
}
\DeclareOption{draft}{   %% Just for downward compatibility
\posterdrafttrue
}
\DeclareOption{posterdraft}{ %% To avoid collisions with the graphics package
\posterdrafttrue
}
\DeclareOption{final}{
\posterdraftfalse
}
\DeclareOption*{\PackageWarning{a0poster}{Unknown Option \CurrentOption}}
\ExecuteOptions{landscape,a0b,final}
\ProcessOptions\relax

\setlength{\paperwidth}{56in}
\setlength{\paperheight}{42in}
\setlength{\textwidth}{53in}
\setlength{\textheight}{39in}

\ifportrait
   \newdimen\spare
   \setlength{\spare}{\paperwidth}
   \setlength{\paperwidth}{\paperheight}
   \setlength{\paperheight}{\spare}
   \setlength{\spare}{\textwidth}
   \setlength{\textwidth}{\textheight}
   \setlength{\textheight}{\spare}
\else\relax
\fi

%% Setting proper dimensions for a DIN A0 printer

\setlength{\headheight}{0 cm}
\setlength{\headsep}{0 cm}
\setlength{\topmargin}{0 cm}
\setlength{\oddsidemargin}{0 cm}

\catcode`\%=11
\newwrite\Edition
\closeout\Edition
\catcode`\%=14

\input{a0size.sty}

\renewcommand{\tiny}{\fontsize{12}{14}\selectfont}
\renewcommand{\scriptsize}{\fontsize{14.4}{18}\selectfont}   
\renewcommand{\footnotesize}{\fontsize{17.28}{22}\selectfont}
\renewcommand{\small}{\fontsize{20.74}{25}\selectfont}
\renewcommand{\normalsize}{\fontsize{24.88}{30}\selectfont}
\renewcommand{\large}{\fontsize{29.86}{37}\selectfont}
\renewcommand{\Large}{\fontsize{35.83}{45}\selectfont}
\renewcommand{\LARGE}{\fontsize{43}{54}\selectfont}
\renewcommand{\huge}{\fontsize{51.6}{64}\selectfont}
\renewcommand{\Huge}{\fontsize{61.92}{77}\selectfont}
\newcommand{\veryHuge}{\fontsize{74.3}{93}\selectfont}
\newcommand{\VeryHuge}{\fontsize{89.16}{112}\selectfont}
\newcommand{\VERYHuge}{\fontsize{107}{134}\selectfont}

\setlength\smallskipamount{6pt plus 2pt minus 2pt}
\setlength\medskipamount{12pt plus 4pt minus 4pt}
\setlength\bigskipamount{24pt plus 8pt minus 8pt}

\setlength\abovecaptionskip{25pt}
\setlength\belowcaptionskip{0pt}
\setlength\abovedisplayskip{25pt plus 6pt minus 15 pt}
\setlength\abovedisplayshortskip{0pt plus 6pt}
\setlength\belowdisplayshortskip{13pt plus 7pt minus 6pt}
\setlength\belowdisplayskip\abovedisplayskip

\normalsize

\AtBeginDocument{
\ifanullb
   \ifportrait\special{papersize=42in,56in}\else\special{papersize=56in,42in}\fi
\else\ifanull
        \ifportrait\special{papersize=42in,56in}\else\special{papersize=56in,42in}\fi
     \else\ifaeins
             \ifportrait\special{papersize=42in,56in}\else\special{papersize=56in,42in}\fi
          \else\ifazwei
                  \ifportrait\special{papersize=42in,56in}\else\special{papersize=56in,42in}\fi
               \else\ifadrei
                      \ifposterdraft
                       \ifportrait\special{papersize=42in,56in}\else\special{papersize=56in,42in}\fi
                      \else
                       \ifportrait\special{papersize=42in,56in}\fi
                      \fi
                    \else\relax
                    \fi
               \fi
          \fi
     \fi
\fi
\pagestyle{empty}}

\endinput
%% 
%% End of file `a0poster.cls'.