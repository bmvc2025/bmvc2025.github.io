---
layout: default_sparse
title: Reviewing Guidelines
permalink: /authors/reviewing-guidelines/
---


<p><strong>These reviewing guidelines are based on best practice from the CVPR 2022 - for further details please see the <a href="https://cvpr2022.thecvf.com/reviewer-guidelines">CVPR Reviewer Guidlines</a>.</strong></p>

<p><strong>To contact the Programme Chairs, please send emails to:</strong></p>
<p style="text-align: center;"><a href="mailto:bmvc2023@googlegroups.com">bmvc2023@googlegroups.com</a></p>

<hr class="wp-block-separator" />

<!--
<h2>Reviewing Timeline</h2>


<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
<table class="table table-striped table-bordered" style="max-width: 750px;">
  <tbody>
    <tr><th scope="row">Deadline</th>
        <th scope="row">Date (all deadlines {{site.deadline-time}})</th></tr>
    {% for item in site.data.timeline.deadlines %}
      {% assign item_is_reviewer = item.tags | where_exp: "i", "i.key == 'reviewers'" %}
      {% if item_is_reviewer.size > 0 %}
        <tr>
            <td>{{item.title}}</td>
            <td>{{item.date | date: '%A %e %b %Y'}}</td>
        </tr>
        {% endif %}
    {% endfor %}
  </tbody>
</table>
</div>


<hr class="wp-block-separator" />
-->

<h2>Guidelines</h2>

<p dir="ltr"><strong>Blind Reviews</strong></p>

<p dir="ltr">Our <a href="{{site.baseurl}}{% link authors/submit-your-paper.md %}">Author Guidelines</a> have instructed authors to make reasonable efforts to hide their identities, including omitting their names, affiliations, and acknowledgments. This information will of course be included in the published version. Likewise, reviewers should make all efforts to keep their identity invisible to the authors.</p>

<p dir="ltr">With the increase in popularity of arXiv preprints, sometimes the authors of a paper may be known to the reviewer. Posting to arXiv is NOT considered a violation of anonymity on the part of the authors, and in most cases, reviewers who happen to know (or suspect) the authors’ identity can still review the paper as long as they feel that they can do an impartial job. An important general principle is to make every effort to treat papers fairly whether or not you know (or suspect) who wrote them. If you do not know the identity of the authors at the start of the process, DO NOT attempt to discover them by searching the Web for preprints.</p>

<p dir="ltr">Please read the FAQ at the end of this document for further guidelines on how arXiv prior work should be handled.</p>

<p dir="ltr"><strong>Check your papers</strong></p>

<p dir="ltr">As soon as you get your reviewing assignment, please go through all the papers to make sure that (a) there is no obvious conflict with you (e.g., a paper authored by your recent collaborator from a different institution) and (b) you feel comfortable to review the paper assigned. If either of these issues arise, please let us know right away by emailing the Program Chairs.</p>

<p dir="ltr">Please read the <a href="{{site.baseurl}}{% link authors/submit-your-paper.md %}">Author Guidelines</a>&nbsp;carefully to familiarize yourself with all official policies (such as double submission and plagiarism). If you think a paper may be in violation of one of these policies, please contact the Program Chairs. In the meantime, proceed to review the paper assuming no violation has taken place.</p>

<p dir="ltr"><strong>What to Look For</strong></p>

<p dir="ltr">Each paper that is accepted should be technically sound and make a contribution to the field. Look for what's good or stimulating in the paper. We recommend that you embrace novel, brave concepts, even if they have not been tested on many datasets. For example, the fact that a proposed method does not exceed the state-of-the-art accuracy on an existing benchmark dataset is not grounds for rejection by itself. Rather, it is important to weigh both the novelty and potential impact of the work alongside the reported performance. Minor flaws that can be easily corrected should not be a reason to reject a paper.</p>

<p dir="ltr"><strong>Check for Reproducibility</strong></p>

<p dir="ltr">To improve reproducibility in AI research, we highly encourage authors to voluntarily submit their code as part of supplementary material, especially if they plan to release it upon acceptance. Reviewers may optionally check this code to ensure the paper’s results are reproducible and trustworthy, but are not required to. Reviewers are also encouraged to use the <a href="https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf">Reproducibility Checklist</a> as a guide for assessing whether a paper is reproducible or not. All code/data should be reviewed confidentially and kept private, and deleted after the review process is complete. We expect (but do not require) that the accompanying code will be submitted with accepted papers.&nbsp;</p>

<p dir="ltr"><strong>Be Specific</strong></p>

<p dir="ltr">Please be specific and detailed in your reviews. Your main critique of the paper should be written in terms of a list of strengths and weaknesses. You can use bullet points here, but also explain your arguments. Your discussion, more than your score, will help the authors, fellow reviewers, and Area Chairs understand the basis for your recommendation, so please be thorough. You should include specific feedback on ways the authors can improve their papers.</p>

<p dir="ltr">In the discussion of related work and references, simply saying "this is well known" or "this has been common practice in the industry for years" is not sufficient: cite specific publications, including books or public disclosures of techniques.</p>

<p dir="ltr">Please read the FAQ at the end of this document for further details on how to treat related work on arXiv, supplementary material, and rebuttals.</p>

<h4 dir="ltr" id="ethics-for-reviewing-papers">Ethics for Reviewing Papers</h4>

<p dir="ltr"><strong>1. Protect Ideas</strong></p>

<p dir="ltr">As a reviewer, you have the responsibility to protect the confidentiality of the ideas represented in the papers you review. Submissions for review are not published documents. The work is considered new or proprietary by the authors; otherwise they would not have submitted it. Of course, their intent is to ultimately publish to the world, but most of the submitted papers will not appear in the proceedings. Thus, it is likely that the paper you have in your hands will be refined further and submitted to some other journal or conference. Sometimes the work is still considered confidential by the authors' employers. These organizations do not consider sending a paper for review to constitute a public disclosure. Protection of the ideas in the papers you receive means:</p>

<ul>
    <li dir="ltr">
    <p dir="ltr">You should not show the paper to anyone else, including colleagues or students, unless you have asked them to write a review, or to help with your review.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You should not show any results, videos/images, code or any of the supplementary material to non-reviewers.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You should not use ideas/code from papers you review to develop your own ideas/code.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">After the review process, you should destroy all copies of papers and supplementary material and erase any code that the authors submitted as part of the supplementary, and any implementations you have written to evaluate the ideas in the papers, as well as any results of those implementations.</p>
    </li>
</ul>

<p dir="ltr"><strong>2. Avoid Conflict of Interest</strong></p>

<p dir="ltr">As a reviewer it is important for you to avoid any conflict of interest. There should be absolutely no question about the impartiality of any review. Thus, if you are assigned a paper where your review would create a possible conflict of interest, you should return the paper and not submit a review. Conflicts of interest include (but are not limited to) situations in which:</p>

<ul>
    <li dir="ltr">
    <p dir="ltr">You work at the same institution as one of the authors.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You have been directly involved in the work and will be receiving credit in some way. If you're a member of the author's thesis committee, and the paper is about his or her thesis work, then you were involved.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You suspect that others might perceive a conflict of interest in your involvement.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You have collaborated with one of the authors in the past three years (more or less). Collaboration is usually defined as having written a paper or grant proposal together, although you should use your judgment.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You were the MSc/PhD advisor or advisee of one of the authors. Most funding agencies and publications typically consider advisees to represent a lifetime conflict of interest. Conferences have traditionally been more flexible than this, but you should think carefully before reviewing a paper you know to be written by a former advisor or advisee, especially a recent one.</p>
    </li>
</ul>

<p dir="ltr">While the organizers make every effort to avoid such conflicts in the review assignments, they may nonetheless occasionally arise. If you recognize the work or the author and feel it could present a conflict of interest, email the Program Chairs as soon as possible so they can find someone else to review it.</p>

<p dir="ltr"><strong>3. Be Professional</strong></p>

<p dir="ltr">Belittling or sarcastic comments have no place in the reviewing process. The most valuable comments in a review are those that help the authors understand the shortcomings of their work and how they might improve it. Write a courteous, informative, incisive, and helpful review that you would be proud to sign with your name (were it not anonymous).</p>

<p dir="ltr"><strong>4. Large Language Model Ethics</strong></p>

<p dir="ltr">In line with other conferences (e.g., <a href="https://iccv2023.thecvf.com/ethics.for.reviewing.papers-362100-2-16-21.php">ICCV</a>), we will adopt a similar approach of not allowing Large Language Models or online chatbots, such as ChatGPT, in any part of the reviewing process.</p>

<h4 dir="ltr">Additional Tips for Writing Good Reviews</h4>

<ul>
    <li dir="ltr">
    <p dir="ltr">Take the time to write good reviews. Ideally, you should read a paper and then think about it over the course of several days before you write your review.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Short reviews are unhelpful to authors, other reviewers, and Area Chairs. If you have agreed to review a paper, you should take enough time to write a thoughtful and detailed review.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Be specific when you suggest that the writing needs to be improved. If there is a particular section that is unclear, point it out and give suggestions for how it can be clarified.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Be specific about novelty. Claims in a review that the submitted work "has been done before" MUST be backed up with specific references and an explanation of how closely they are related. At the same time, for a positive review, be sure to summarize what novel aspects are most interesting in the Strengths section.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Do not reject papers solely because they are missing citations or comparisons to prior work that has only been published without review (e.g., arXiv or technical reports). Refer to the FAQ below for more details on handling arXiv prior art.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Don't give away your identity by asking the authors to cite several of your own papers.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">If you think the paper is out of scope for the conference subject areas, clearly explain why in the review. Then suggest other publication possibilities (journals, conferences, workshops) that would be a better match for the paper. However, unless area mismatch is extreme, you should keep an open mind, because we want a diverse set of good papers at the conference.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">The tone of your review is important. A harshly written review will be resented by the authors, regardless of whether your criticisms are true. If you take care, it is always possible to word your review constructively while staying true to your thoughts about the paper.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Avoid referring to the authors in the second person ("you"). Instead, use the third person ("the authors" or "the paper"). Referring to the authors as "you" can be perceived as being confrontational, even though you may not mean it this way.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Be generous about giving the authors new ideas for how they can improve their work. You might suggest a new technical tool that could help, a dataset that could be tried, an application area that might benefit from their work, or a way to generalize their idea to increase its impact.</p>
    </li>
</ul>

<p dir="ltr">Finally, keep in mind that a thoughtful review not only benefits the authors, but also yourself. Your reviews are read by other reviewers and especially the Area Chairs, in addition to the authors. Being a helpful reviewer will generate good will towards you in the research community -- and may even help you to win an Outstanding Reviewer award.</p>

<h4 dir="ltr" id="cmt-instructions">CMT Instructions</h4>

<p dir="ltr">Once you've been notified by email that papers have been assigned to you, please log into the CMT site (<a href="{{site.cmt-url}}">{{site.cmt-url}}</a>), choose the “Reviewer” role on top, and follow the steps below.</p>

<p dir="ltr"><strong>1. Download your papers.</strong></p>

<p dir="ltr">To download individual papers, you can click the links underneath individual paper titles. Or, you can click the “Actions” button in the top right corner and then choose “Download Files”. This allows you to download a zip file containing all the papers plus supplementary files (if available).</p>

<p dir="ltr"><strong>2. Check for possible conflict or submission rule violations.</strong></p>

<p dir="ltr">Contact the Program Chairs immediately if:</p>

<ol>
    <li dir="ltr">
    <p dir="ltr">You think you are conflicted with the paper (see the section entitled “Avoid Conflict of Interest” above).</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">You think the paper violates submission rules regarding anonymity, double submission, or plagiarism (please refer to <a href="{{site.baseurl}}{% link authors/submit-your-paper.md %}">Author Guidelines</a>&nbsp;for precise definitions of what is and isn’t considered acceptable). In the meantime, go ahead and review the paper as if there is no violation. The Program Chairs will follow up, but it may take a bit of time.</p>
    </li>
</ol>

<p dir="ltr"><strong>3. Review papers and assign them a preliminary (pre-rebuttal) rating.</strong></p>

<p dir="ltr">For a paper, under the review column, click "Edit Review" to get to the review form. You can hover the mouse over the “?” symbol next to each question for a more detailed explanation, in particular, for the interpretations of paper ratings in questions 4 and 10. Before you start writing your reviews, make sure you have read the Reviewer Guidelines above and the <a href="https://cvpr2022.thecvf.com/sites/default/files/2021-11/How%20to%20be%20a%20good%20reviewer-tutorials%20for%20cvpr2022%20reviewers.pptx.pdf">CVPR 202 Reviewer Tutorial</a>.</p>

<p dir="ltr"><strong>4. (Optional) Review papers offline.</strong></p>

<p dir="ltr">To enable offline reviewing, go to “Actions - &gt; Import Reviews”. You can select papers and click “Download” to obtain XML review stubs and the update files as needed. Once you are done updating, you can upload the file from the same page. We suggest that you use an XML editor to edit the file. You should always verify the review after uploading by inspecting it online.</p>

<p dir="ltr"><strong>5. Participate in discussions with Area Chairs and other reviewers.</strong></p>

<p dir="ltr">After the rebuttal period, reviewers will work with Area Chairs to clear up any confusions and attempt to reach consensus on papers. The CMT site has an electronic bulletin board feature that allows Area Chairs to contact reviewers anonymously. Once the Area Chair posts a note, reviewers will be notified and asked to log in to see the post and respond. The identities of the reviewers will be hidden from each other (but not from the Area Chair).</p>

<p dir="ltr"><strong>6. Enter your final (post-rebuttal) recommendation.</strong></p>

<p dir="ltr">After the rebuttal/revision period you will enter your final recommendation on CMT. This may differ from your preliminary rating, and should reflect your judgment taking into account all the other reviews, the authors' rebuttal/revision, and the discussion about the paper (if any).</p>

<h4 dir="ltr" id="reviewer-faqs">Reviewer FAQs</h4>

<p>Q. How should code submission be handled?<br />
A. Please read the Author FAQ regarding code submission.</p>

<p dir="ltr">Q. Is there a minimum number of papers I should accept or reject?<br />
A. No. Each paper should be evaluated in its own right. If you feel that most of the papers assigned to you have value, you should accept them. It is unlikely that most papers are bad enough to justify rejecting them all. However, if that is the case, provide clear and very specific comments in each review. Do NOT assume that your stack of papers necessarily should have the same acceptance rate as the entire conference ultimately will.</p>

<p dir="ltr">Q. Can I review a paper I already saw on arXiv and hence know who the authors are?<br />
A. In general, yes, unless you are conflicted with one of the authors. See next question below for guidelines.</p>

<p dir="ltr">Q. How should I treat papers for which I know the authors?<br />
A. Reviewers should make every effort to treat each paper impartially, whether or not they know who wrote the paper. For example: It is not OK for a reviewer to read a paper, think "I know who wrote this; it's on arXiv; they are usually quite good" and accept the paper based on that reasoning. Conversely, it is also not OK for a reviewer to read a paper, think "I know who wrote this; it's on arXiv; they are no good" and reject paper based on that reasoning.</p>

<p dir="ltr">Q. Should authors be expected to cite related arXiv papers or compare to their results?<br />
A. Consistent with good academic practice, the authors should cite all sources that inspired and informed their work. This said, asking authors to thoroughly compare their work with arXiv reports that appeared shortly before the submission deadline imposes an unreasonable burden. We also do not wish to discourage the publication of similar ideas that have been developed independently and concurrently. Reviewers should keep the following guidelines in mind:</p>

<ul>
    <li dir="ltr">
    <p dir="ltr">Authors are not required to discuss and compare their work with recent arXiv reports, although they should properly acknowledge those that directly and obviously inspired them.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Failing to cite an arXiv paper or failing to beat its performance SHOULD NOT be sole grounds for rejection.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">Reviewers SHOULD NOT reject a paper solely because another paper with a similar idea has already appeared on arXiv. If the reviewer suspects plagiarism or academic dishonesty, they are encouraged to bring these concerns to the attention of the Program Chairs.</p>
    </li>
    <li dir="ltr">
    <p dir="ltr">It is acceptable for a reviewer to suggest that an author should acknowledge or be aware of something on arXiv.</p>
    </li>
</ul>

<p>Q. How should I treat the supplementary material?<br />
A. The supplementary material is intended to provide details of derivations and results that do not fit within the paper format or space limit. Ideally, the paper should indicate when to refer to the supplementary material, and you need to consult the supplementary material only if you think it is helpful in understanding the paper and its contribution. According to the Author Guidelines, the supplementary material MAY NOT include results on additional datasets, results obtained with an improved version of the method (e.g., following additional parameter tuning or training), or an updated or corrected version of the submission PDF. If you find that the supplementary material violates these guidelines, please contact the Program Chairs.</p>

<!--
Q. Can I request additional experiments in the author rebuttal/revision? How should I treat additional experiments reported by authors in the rebuttal/revision?<br />
A. In your review, you may request clarifications or additional illustrations in the rebuttal/revision. Reviewers may ask for new experiments if they feel that it is essential for the paper to be accepted **but** reviewers should take into account that authors only have 2 weeks for rebuttal/revision and should therefore not request more substantial experiments.
-->
