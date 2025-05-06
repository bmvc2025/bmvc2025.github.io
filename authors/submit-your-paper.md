---
layout: default_sparse
title: Submit Your Paper
permalink: /authors/submit-your-paper/
index: 2
---

## Abstract and Paper Submission

<p>Abstract and paper submissions are handled via OpenReview. The submission portal can be accessed by clicking on the following button, as well as instructions on how to create a profile in OpenReview if this is your first time using OpenReview.</p>

<div class="row no-gutters pt-0 d-xs-block ">
    <div class="mb-1 pl-2 pr-2 mx-auto mx-sm-left col-xs-auto">
        <p style="text-align: center;"><a class="btn btn-primary" role="button" href="https://openreview.net/group?id=bmva.org/BMVC/2025/Conference">Submit your Paper via OpenReview</a></p>
    </div>
    <div class="mb-1 pl-2 pr-2 mx-auto mx-sm-left col-xs-auto">
        <p style="text-align: center;"><a class="btn btn-primary" role="button" href="https://docs.openreview.net/getting-started/creating-an-openreview-profile">How to create an OpenReview Account</a></p>
    </div>
</div>

<!-- **<span style="color:red">Authors who will use a personal email (e.g. gmail, etc.) to sign up to OpenReview for the first time, need to create an OpenReview profile asap! This is because it can take up to 2 weeks for profiles using public email services to be activated.</span>** -->

Abstract registration is performed by registering as a user with OpenReview and entering a paper title and abstract. This will result in the allocation of a “paper ID”, which indicates that registration is completed and should be used to prepare the review copy. You can make edits and upload new paper drafts until the final paper deadline. Submitted papers should be prepared according to the published specifications for formatting and style. Please be sure to read both the [formatting instructions]({{site.baseurl}}{% link authors/submit-your-paper.md %}#typesetting) and the [Author Guidelines]({{site.baseurl}}{% link authors/author-guidelines.md %}) before submission.

---
## Formatting your paper

A complete paper should be submitted according to the formatting style ([please see below under typesetting]({{site.baseurl}}{% link authors/submit-your-paper.md %}#typesetting)). 

#### Submitted paper (for review)

Papers submitted for review should be anonymous and instead include the paper ID allocated by OpenReview upon registration of the abstract/paper. The addition of line numbers (automatic in the PDFLaTeX template) should be included to facilitate the review process.

**Page limit:** A complete paper should be submitted according to the [formatting style]({{site.baseurl}}{% link authors/submit-your-paper.md %}#typesetting). **The length of papers submitted for review should not exceed NINE pages, excluding the references.** All appendices must be supplied as supplementary material, in a separate file to the main paper, and do not count towards the NINE pages limit ([see below for instructions about the supplementary material]({{site.baseurl}}{% link authors/submit-your-paper.md %}#supplementary-material))

#### Typesetting

<p>Typesetting should be done using the <strong>PDFLaTeX system</strong> (part of all modern LaTeX distributions). However, submissions prepared in Microsoft Word or OpenOffice may be accepted in exceptional circumstances. Still, it is the authors' responsibility to match their paper to the PDFLaTeX system. </p>

<p>Paper templates, along with example PDF outputs, are available for download through GitHub: </p>

<div class="row no-gutters pt-0 d-xs-block ">
    <div class="mb-1 pl-2 pr-2 mx-auto mx-sm-left col-xs-auto">
        <p style="text-align: center;"><a class="btn btn-primary" role="button" href="https://github.com/BritishMachineVisionAssociation/BMVCTemplate">View the Github repository</a></p>
    </div>
    <div class="mb-1 pl-2 pr-2 mx-auto mx-sm-left col-xs-auto">
         <p style="text-align: center;"><a class="btn btn-primary" role="button" href="https://www.overleaf.com/latex/templates/author-guidelines-for-the-british-machine-vision-conference-2025/wtpstkznrwgf">Get Overleaf Template</a></p>
     </div>
</div>

<p>Instructions on how to use the BMVC LaTeX template are described in the README.md file within the repository. To enable review mode in the LaTeX template, the <code>\bmvcreviewcopy{??}</code> command should be used, where <code>??</code> is your assigned paper number.</p>

<p><strong>For the camera ready copy</strong>, the <code>\bmvcreviewcopy{??}</code> command should be removed. Also, remember to de-anonymise, have the same order and number of authors as stated in the OpenReview submission, and you can add an extra page of content to the camera-ready version of your paper.</p>

<p></p>

#### Supplementary material

<p>Authors may optionally upload supplementary material, which may include:</p>

<ul>
<li>Videos to showcase results/demo of the proposed approach/system</li>
<li>Images and other results in addition to the ones in the paper</li>
<li>Anonymised related submissions to other conferences and journals</li>
<li>Appendices or technical reports containing extended proofs and mathematical derivations that are not essential to the understanding of the submitted paper</li>
</ul>

<p><strong>Supplementary material should be uploaded as a single ZIP file (up to 100MB) to the OpenReview website.</strong></p>

The authors should appropriately refer to the supplementary material in the paper. Note that reviewers will be encouraged to look at it but are not obligated to do so. 

Supplementary material is to be submitted by the [supplemental material deadline]({{site.baseurl}}{% link dates.md %}).

<!-- <p style="text-align: center;"><a class="btn btn-primary" role="button" href="" disabled>Submit your Paper via OpenReview</a></p> -->


---
## Camera ready copy (for accepted papers)

Camera-ready submissions for accepted papers can be completed via [OpenReview](https://openreview.net/group?id=bmva.org/BMVC/2025/Conference). All papers will require one author to pay a registration fee. This will cover the costs of hosting the conference and proceedings. Papers for which no registered authors will be removed from the conference. For each accepted paper, authors should upload the following:

* Final camera-ready paper (in PDF format)
* Optional supplementary materials (ZIP file up to 100MB)
* The name of your submission file must be of the form XXXX.pdf, where XXXX is the paper ID (zero-padded if necessary). For example, if your paper ID is 24, the filename must be 0024.pdf. If you upload supplementary materials, please name them as XXXX_supp.zip, where XXXX is the four-digit paper ID (zero-padded if necessary).

**The paper length** of the final version must not exceed **10 pages**, *not counting* the acknowledgment and bibliography. **Only** the acknowledgment and bibliography should be *excluded* from the page count: **all** appendices must be counted within the *10-page* limit. or supplied as supplementary material. Papers must not have altered margins and formatting from those laid down by this style guide. The bibliography should begin immediately after the paper text. It may be of any length, within reason. It must *not* include annotations, figures, or any other paraphernalia intended to subvert the paper length requirement.
